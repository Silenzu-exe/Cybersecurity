---
tags: [networking, cybersecurity, wireshark, tcpdump, packets, cheatsheet]
---

# 08 — Packet Analysis (Wireshark & tcpdump)

---

## What is Packet Analysis?

Capturing and inspecting network traffic at the raw packet level. Used for:
- **CTF challenges** — `.pcap` files are common CTF artifacts
- **Incident response** — replaying traffic to understand what an attacker did
- **Recon** — sniffing credentials/data on unencrypted connections
- **Protocol learning** — see exactly what HTTP, DNS, TCP look like in practice

---

## tcpdump (CLI — works on Termux + your Arch box)

**Basic capture:**
```bash
sudo tcpdump -i eth0                      # capture on interface eth0
sudo tcpdump -i any                        # capture all interfaces
sudo tcpdump -i eth0 -w capture.pcap        # write to file (open in Wireshark later)
sudo tcpdump -r capture.pcap                 # read from file
sudo tcpdump -i eth0 -c 100                   # capture only 100 packets
sudo tcpdump -i eth0 -v / -vv / -vvv           # verbosity levels
sudo tcpdump -i eth0 -n                         # don't resolve hostnames (faster, cleaner)
sudo tcpdump -i eth0 -nn                         # don't resolve hostnames OR port names
sudo tcpdump -i eth0 -X                           # show hex + ASCII content
sudo tcpdump -i eth0 -A                            # show ASCII only (good for HTTP)
```

**Filters (BPF — Berkeley Packet Filter):**
```bash
# By host
tcpdump host 192.168.1.10                    # to/from this IP
tcpdump src 192.168.1.10                      # source only
tcpdump dst 192.168.1.10                       # destination only

# By port
tcpdump port 80                               # HTTP
tcpdump port 443                               # HTTPS
tcpdump port not 22                             # everything except SSH

# By protocol
tcpdump tcp
tcpdump udp
tcpdump icmp

# Combining filters
tcpdump host 10.0.0.1 and port 80
tcpdump host 10.0.0.1 or host 10.0.0.2
tcpdump not port 22 and not port 443

# Practical security filters
tcpdump -i eth0 -A port 80                    # read HTTP in plaintext
tcpdump -i eth0 port 21                        # watch FTP (creds visible)
tcpdump -i eth0 icmp                            # only ICMP (ping traffic)
tcpdump -i eth0 arp                              # ARP traffic (spot ARP spoofing)
```

---

## Wireshark (GUI — for .pcap analysis)

### Display Filters (live or on a pcap file)

> [!tip] Display filters ≠ capture filters
> Wireshark's display filters (the bar at the top) use a different syntax from tcpdump's BPF filters. Both are useful — don't confuse them.

**Protocol filters:**
```
http
tcp
udp
dns
ftp
ssh
icmp
arp
smb
```

**IP/Port filters:**
```
ip.addr == 192.168.1.10           # traffic to/from this IP
ip.src == 192.168.1.10             # source
ip.dst == 192.168.1.10              # destination
tcp.port == 80
tcp.dstport == 443
udp.port == 53
```

**Content/string search:**
```
http.request                          # only HTTP requests
http.response.code == 200              # HTTP 200 OK
http.request.method == "POST"           # POST requests (login forms!)
http contains "password"                 # find the word password in HTTP traffic
frame contains "flag"                     # search for CTF flags
dns.qry.name contains "google"            # DNS queries for google
```

**TCP flag filters:**
```
tcp.flags.syn == 1                    # SYN packets
tcp.flags.syn == 1 && tcp.flags.ack == 0     # SYN only (new connections)
tcp.flags.reset == 1                           # RST packets (dropped connections)
tcp.flags == 0x002                              # hex — SYN only
```

**Combining:**
```
http && ip.src == 192.168.1.5
dns && ip.addr == 8.8.8.8
tcp.port == 21 || tcp.port == 20
```

---

## Wireshark — Useful Menu Features

| Feature | Where | What it does |
|---|---|---|
| Follow TCP Stream | Right-click packet → "Follow" → "TCP Stream" | Reassembles full conversation — great for reading HTTP, FTP, plaintext protocols |
| Follow HTTP Stream | Right-click → Follow → HTTP | Same but decoded HTTP |
| Export Objects | File → Export Objects → HTTP | Extract files transferred over HTTP (images, downloads, etc.) |
| Statistics → Protocol Hierarchy | Statistics menu | See breakdown of all protocols in the capture |
| Statistics → Conversations | Statistics menu | See all connections — who talked to who |
| Statistics → IO Graph | Statistics menu | Traffic volume over time — spikes = potential DoS, exfil |
| Edit → Find Packet | Ctrl+F | Search for string, hex, or regex in packets |

---

## CTF — Common .pcap Scenarios

| What you see | What to do |
|---|---|
| HTTP traffic | Follow TCP stream → look for credentials, flags, file transfers |
| FTP traffic | Follow TCP stream → credentials in plaintext |
| DNS queries | Filter `dns` → look for unusual queries, long subdomains (DNS tunneling) |
| ICMP traffic | Filter `icmp` → check data field for hidden content (ICMP tunneling) |
| Many SYN with no SYN-ACK | Port scan or SYN flood in progress |
| ARP replies flooding | ARP spoofing / MITM attack |
| Huge file in HTTP | Export Objects → recover the file |
| Encrypted traffic + TLS keys file provided | Load key in Wireshark: Edit → Preferences → TLS → add key file |
| Long base64-looking DNS queries | DNS tunneling — data exfiltration |

---

## Quick Analysis Workflow for a .pcap file

```
1. Open in Wireshark
2. Statistics → Protocol Hierarchy  (what protocols are present?)
3. Statistics → Conversations        (who's talking to who, how much data?)
4. Filter by interesting protocols   (http, ftp, dns, smb)
5. Follow TCP streams on anything interesting
6. Look for credentials in HTTP POST bodies, FTP, Telnet
7. Export Objects if HTTP file transfers visible
8. Check for flags (Ctrl+F → search "flag" or "CTF" or the flag format)
```
