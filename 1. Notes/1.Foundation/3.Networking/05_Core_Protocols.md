---
tags: [networking, cybersecurity, protocols, cheatsheet]
---

# 05 — Core Protocols

A protocol is a set of rules for formatting and processing data — a common language that lets very different devices communicate with each other regardless of their underlying software/hardware.

> [!note] HTTP/HTTPS and DNS have their own dedicated files
> See [[04_HTTP_and_HTTPS]] and [[03_DNS]] for those two — this file covers everything else.

---

## FTP (File Transfer Protocol) — Port 20/21

| Mode | Port | What it's for |
|---|---|---|
| Control | 21 | Commands (login, directory, etc.) |
| Data | 20 (active) / random (passive) | Actual file transfer |

> [!warning] Security issues
> - Credentials and data sent in **plaintext** — easily sniffed with Wireshark
> - **Anonymous login** often enabled by default on old servers: `ftp target.com` → user `anonymous`, password anything
> - Brute-forceable with Hydra
> - Use **SFTP** (SSH-based, port 22) or **FTPS** (FTP over TLS) instead

---

## SSH (Secure Shell) — Port 22

Encrypted remote access. Your primary tool for OverTheWire, HTB, VPS management.

```bash
ssh user@host                         # basic
ssh -p 2222 user@host                   # custom port
ssh -i ~/.ssh/id_rsa user@host           # use specific key file
ssh -L 8080:localhost:80 user@host        # local port forward
ssh -D 9050 user@host                      # SOCKS proxy (for tunneling)
```

**Key-based auth:**
```bash
ssh-keygen -t ed25519 -C "label"        # generate key pair
ssh-copy-id user@host                    # push public key to server
cat ~/.ssh/authorized_keys               # view allowed keys on a server
```

> [!note] Security relevance
> - Weak/reused passwords = brute-force target (Hydra, Medusa)
> - Old SSH versions have known CVEs — version fingerprinting via nmap reveals this
> - Misconfigured `authorized_keys` is a persistence technique attackers use

---

## Telnet (Teletype Network) — Port 23

A protocol for remote terminal connection. The `telnet` client lets you connect to and issue text commands to any server listening on a TCP port — originally for remote administration, but useful generally for **banner grabbing** against any TCP service.

```bash
telnet target 25       # connect to SMTP, read the banner
telnet target 80        # manually issue an HTTP request
```

> [!warning] Security issue
> Fully plaintext — including any credentials typed during a session. Superseded by SSH for remote administration, but still occasionally found exposed.

---

## SMTP / Email Protocols

| Protocol | Port | Purpose | Encrypted version |
|---|---|---|---|
| SMTP | 25 / 587 | Sending mail | SMTPS (465) or STARTTLS |
| POP3 | 110 | Receive (download) | POP3S (995) |
| IMAP | 143 | Receive (sync) | IMAPS (993) |

> [!note] Security relevance
> - SMTP on port 25 is often open on servers and can be used for **user enumeration** (`VRFY username`)
> - **Email spoofing** abuses open relays — check SPF, DKIM, DMARC records via TXT DNS records ([[03_DNS]])

---

## ARP (Address Resolution Protocol)

**What it does:** Maps IP addresses → MAC addresses on the local network so devices can find each other's physical/hardware identifier. Operates at Layer 2 — **zero authentication**, anyone can reply.

**How it works:**
1. Every device keeps an **ARP cache** — a log of known IP → MAC mappings.
2. To find a device, a computer broadcasts an **ARP Request**: "Who has this IP address?"
3. Only the device that owns that IP responds with an **ARP Reply** containing its MAC address.
4. The requester stores this mapping in its ARP cache for future use.

```
Who has 192.168.1.1?  → ARP Request (broadcast)
I do! My MAC is XX:XX  → ARP Reply
```

> [!warning] Security relevance
> ARP's lack of authentication is the root cause of **ARP spoofing/poisoning**, where an attacker replies to ARP requests with their own MAC to intercept traffic (MITM) — full attack details in [[09_Network_Attacks]].

---

## DHCP (Dynamic Host Configuration Protocol)

**What it does:** Automatically assigns IP addresses to devices joining a network (the alternative is manually configuring each device).

**The 4-step handshake (DORA):**
1. **Discover** — device broadcasts looking for any DHCP server on the network.
2. **Offer** — a DHCP server replies with an available IP address.
3. **Request** — the device replies confirming it wants that offered IP.
4. **Acknowledge (ACK)** — the DHCP server confirms, and the device can start using the IP.

```
Client → Discover → (broadcast)
Server → Offer     → Client
Client → Request   → Server
Server → ACK       → Client
```

> [!warning] Security relevance
> A **rogue DHCP server** can hand out malicious configuration (e.g. a fake gateway or DNS server), redirecting a victim's traffic through an attacker-controlled path.

---

## ICMP (Internet Control Message Protocol)

Used for diagnostics (ping, traceroute). Operates at Layer 3.

```bash
ping host            # sends ICMP echo request, expects echo reply
traceroute host       # ICMP TTL manipulation to map the route
```

> [!note] Security relevance
> - **ICMP can be blocked** by firewalls — a non-responsive host ≠ host is offline
> - **Ping sweeps** (`nmap -sn`) use ICMP to discover live hosts
> - **ICMP tunneling** — data can be hidden inside ICMP packets (exfiltration technique)

---

## SNMP (Simple Network Management Protocol) — Port 161/162

Used to monitor and manage network devices (routers, switches, printers).

> [!warning] Security relevance
> - SNMPv1/v2c use **community strings** (default: `public`, `private`) as passwords — often unchanged
> - Can leak **device info, routing tables, running processes** if the public community string is accessible
> - `snmpwalk -c public -v2c target` reveals a lot if misconfigured
> - SNMPv3 has proper auth/encryption — but older versions are everywhere

---

## SMB (Server Message Block) — Port 445 / 139

Windows file/printer sharing protocol. Also present on Linux via Samba.

```bash
smbclient -L //target               # list shares
smbclient //target/sharename         # connect to a share
enum4linux -a target                  # full SMB enumeration
```

> [!warning] Security relevance
> - **EternalBlue (MS17-010)** — the NSA exploit that powered WannaCry ran over SMB (port 445)
> - Null sessions (no auth) can expose shares, user lists, policies on older Windows
> - Always check for open SMB shares during recon — often misconfigured

---

## RDP (Remote Desktop Protocol) — Port 3389

Windows remote desktop.

> [!warning] Security relevance
> - Brute-force target (common; credentials often weak)
> - **BlueKeep (CVE-2019-0708)** — critical pre-auth RCE in older RDP implementations
> - Exposed RDP on the internet = one of the top ransomware entry points in real incidents
