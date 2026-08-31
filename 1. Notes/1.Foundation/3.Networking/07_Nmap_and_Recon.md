---
tags: [networking, cybersecurity, nmap, recon, cheatsheet]
---

# 07 — Nmap & Recon

---

## Nmap Scan Types

| Flag | Scan Type | How it works | When to use |
|---|---|---|---|
| `-sS` | SYN scan (stealth) | Sends SYN, gets SYN-ACK, sends RST (never completes handshake) | Default when root — less noisy |
| `-sT` | TCP Connect | Full 3-way handshake | When non-root, or when `-sS` fails |
| `-sU` | UDP scan | Sends UDP packets, waits for response | Slow but needed for DNS/SNMP/DHCP |
| `-sN` | NULL scan | No flags set — used to evade some firewalls | Stealth; works on Unix, not Windows |
| `-sF` | FIN scan | Only FIN flag | Firewall evasion |
| `-sX` | Xmas scan | FIN+PSH+URG flags | Firewall evasion; doesn't work on Windows |
| `-sA` | ACK scan | Maps firewall rules | Tells you filtered vs. unfiltered |
| `-sn` | Ping sweep | No port scan, just discovers live hosts | Fast network discovery |
| `-Pn` | No ping | Skip host discovery, scan anyway | Use when host blocks ping |

---

## Port Specification

```bash
nmap target                     # top 1000 ports
nmap -p 80                       # single port
nmap -p 80,443,8080               # multiple ports
nmap -p 1-1000                     # range
nmap -p-                            # all 65535 ports
nmap --top-ports 20                  # top 20 most common ports
nmap -p U:53,T:80,443 target         # UDP and TCP together
```

---

## Detection & Version Flags

```bash
-sV          # service version detection (what's running on the port)
-O           # OS detection (requires root)
-A           # aggressive: -sV + -O + script scan + traceroute
--version-intensity 5    # 0-9, higher = more probes (slower)
```

---

## Timing Templates

| Flag | Name | Speed | Use case |
|---|---|---|---|
| `-T0` | Paranoid | Extremely slow | IDS evasion |
| `-T1` | Sneaky | Very slow | Evasion |
| `-T2` | Polite | Slow | Less bandwidth |
| `-T3` | Normal | Default | Normal use |
| `-T4` | Aggressive | Fast | CTFs, lab environments |
| `-T5` | Insane | Very fast | Unreliable — use only on fast LAN |

---

## Nmap Scripting Engine (NSE)

NSE scripts add targeted checks on top of a port scan. Huge force multiplier.

```bash
-sC                          # run default scripts (equivalent to --script=default)
--script=scriptname           # run a specific script
--script=category             # run all scripts in a category
--script-args key=val          # pass arguments to scripts
```

**Script categories:**

| Category | What it does |
|---|---|
| `default` | Safe, informative — runs with `-sC` |
| `safe` | Won't crash services |
| `auth` | Auth-related checks (brute, bypass) |
| `vuln` | Known vulnerability checks |
| `exploit` | Active exploitation (use carefully) |
| `brute` | Brute force |
| `discovery` | Extra info gathering |

**Useful specific scripts:**

```bash
--script=http-title                  # grab page title
--script=http-enum                   # enumerate web directories
--script=smb-vuln-ms17-010           # check for EternalBlue
--script=smb-enum-shares             # list SMB shares
--script=ftp-anon                    # check for anonymous FTP
--script=ssh-brute                   # SSH brute force
--script=dns-zone-transfer           # attempt DNS zone transfer
--script=http-auth-finder            # find pages with auth
--script=vuln                        # run all vuln scripts (noisy but thorough)
--script=banner                      # grab banners from open ports
```

---

## Output Formats

```bash
-oN output.txt          # normal text output (human-readable)
-oX output.xml           # XML (parseable, used by Metasploit)
-oG output.gnmap          # grepable format
-oA output                # all three at once (output.nmap, output.xml, output.gnmap)
-v / -vv                   # verbose / very verbose (see progress live)
```

---

## Common Scan Workflows

**Quick "what's open?" on a target:**
```bash
nmap -T4 --open -Pn target
```

**Full port scan + version + default scripts:**
```bash
nmap -sS -sV -sC -p- -T4 target -oA full_scan
```

**Subnet host discovery:**
```bash
nmap -sn 192.168.1.0/24
```

**Check for common vulns:**
```bash
nmap -sV --script=vuln target
```

**UDP top services (DNS, SNMP, DHCP):**
```bash
sudo nmap -sU --top-ports 20 target
```

---

## Beyond Nmap — Other Recon Tools

### DNS Enumeration
```bash
dig axfr @ns.target.com target.com        # zone transfer attempt
dnsenum target.com                          # full DNS enum
dnsrecon -d target.com                       # recon + subdomain brute force
sublist3r -d target.com                       # passive subdomain discovery
```

### Web Recon
```bash
gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt
gobuster dns -d target.com -w subdomains.txt
nikto -h http://target                       # web server vulnerability scan
whatweb http://target                         # fingerprint web tech (CMS, server, etc.)
curl -I http://target                          # grab HTTP headers
```

### OSINT
```bash
whois target.com                         # registration info + name servers
theHarvester -d target.com -b google      # emails, subdomains, IPs from search engines
shodan search "apache target.com"          # (web) find target on Shodan
```

### Banner Grabbing (manual service fingerprinting)
```bash
nc -v target 80         # connect to port, grab whatever the server sends
curl -v http://target    # verbose — shows request + response headers
telnet target 25         # connect to SMTP, read banner
```

---

## Recon Checklist (for a new target)

```
[ ] Ping / host discovery (nmap -sn)
[ ] Quick top-1000 port scan
[ ] Full port scan (-p-)
[ ] Service/version detection (-sV) on open ports
[ ] Default script scan (-sC) on open ports
[ ] Web: Gobuster + Nikto if 80/443 open
[ ] SMB: enum4linux if 445 open
[ ] DNS: zone transfer attempt if 53 open
[ ] FTP: anonymous login if 21 open
[ ] SNMP: community string walk if 161 open
[ ] Banner grabbing on anything unusual
[ ] OS detection (-O)
[ ] Google / OSINT on domain if applicable
```
