---
tags: [networking, cybersecurity, protocols, cheatsheet]
---

# 02 — Protocols

---

In networking, a protocol is a set of rules for formatting and processing data. Network protocols are like a common language for computers. The computers within a network may use vastly different software and hardware; however, the use of protocols enables them to communicate with each other regardless.

## HTTP / HTTPS

| | HTTP | HTTPS |
|---|---|---|
| Port | 80 | 443 |
| Encryption | None (plaintext) | TLS/SSL |
| Intercept risk | High — anyone on network can read it | Encrypted in transit |

**Key HTTP Methods:**

| Method | Purpose | Security note |
|---|---|---|
| `GET` | Retrieve resource | Params in URL — logged everywhere |
| `POST` | Send data | Body is hidden from URL, but not encrypted without HTTPS |
| `PUT` | Upload/replace resource | Often abused if server misconfigured |
| `DELETE` | Delete resource | Should require auth — often doesn't |
| `OPTIONS` | What methods are allowed | Can reveal attack surface |
| `PATCH` | Partial update | |

**HTTP Status Codes (quick reference):**

| Code | Meaning | Security relevance |
|---|---|---|
| 200 | OK | Normal response |
| 301/302 | Redirect | Can be hijacked |
| 400 | Bad request | Input parsing error |
| 401 | Unauthorized | Auth required |
| 403 | Forbidden | You're blocked, but the resource exists |
| 404 | Not found | |
| 500 | Server error | Can leak stack traces / version info |
| 503 | Service unavailable | May indicate DoS |

---

## DNS (Domain Name System) — Port 53 (UDP/TCP)

**What it does:** Translates domain names → IP addresses.

**Record types:**

| Record | Purpose | Example |
|---|---|---|
| `A` | Domain → IPv4 | `google.com → 142.250.x.x` |
| `AAAA` | Domain → IPv6 | |
| `CNAME` | Alias for another domain | `www → example.com` |
| `MX` | Mail server | `@example.com → mail.example.com` |
| `TXT` | Arbitrary text (SPF, DKIM, verification) | |
| `NS` | Nameservers for a domain | |
| `PTR` | Reverse DNS — IP → domain | |

**Commands:**
```bash
dig domain.com               # full DNS query
dig domain.com MX             # specific record type
dig @8.8.8.8 domain.com       # query a specific DNS server
nslookup domain.com             # simpler alternative
host domain.com                  # quick lookup
```

> [!note] Security relevance
> - **DNS enumeration** reveals subdomains, mail servers, internal names → recon goldmine
> - **DNS poisoning/spoofing**: attacker gives false A records → user goes to wrong IP
> - DNS is often **unencrypted (UDP)** — interceptable on the wire
> - **Zone transfer** (`dig axfr @ns.target.com target.com`) can dump the entire DNS zone if misconfigured

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

## SMTP / Email Protocols

| Protocol | Port | Purpose | Encrypted version |
|---|---|---|---|
| SMTP | 25 / 587 | Sending mail | SMTPS (465) or STARTTLS |
| POP3 | 110 | Receive (download) | POP3S (995) |
| IMAP | 143 | Receive (sync) | IMAPS (993) |

> [!note] Security relevance
> - SMTP on port 25 is often open on servers and can be used for **user enumeration** (`VRFY username`)
> - **Email spoofing** abuses open relays — check SPF, DKIM, DMARC records via TXT DNS

---

## ARP (Address Resolution Protocol)

**What it does:** Maps IP addresses → MAC addresses on a local network.
**Operates at:** Layer 2 (no authentication — anyone can reply).

```
Who has 192.168.1.1?  → ARP Request (broadcast)
I do! My MAC is XX:XX  → ARP Reply
```

> [!warning] Security relevance
> ARP has **zero authentication** — this is the root cause of **ARP spoofing/poisoning**, where an attacker replies to ARP requests with their own MAC address to intercept traffic (MITM).

---

## ICMP (Internet Control Message Protocol)

Used for diagnostics (ping, traceroute). Operates at Layer 3.

```bash
ping host            # sends ICMP echo request, expects echo reply
traceroute host       # ICMP TTL manipulation to map the route
```

> [!note] Security relevance
> - **ICMP can be blocked** by firewalls — a non-responsive host ≠ host is offline
> - **Ping sweeps** (nmap -sn) use ICMP to discover live hosts
> - **ICMP tunneling** — data can be hidden inside ICMP packets (exfiltration technique)

---

## SNMP (Simple Network Management Protocol) — Port 161/162

Used to monitor and manage network devices (routers, switches, printers).

> [!warning] Security relevance
> - SNMPv1/v2c use **community strings** (default: `public`, `private`) as passwords — often unchanged
> - Can leak **device info, routing tables, running processes** if public community string is accessible
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
> - Brute-force target (common + credentials often weak)
> - **BlueKeep (CVE-2019-0708)** — critical pre-auth RCE in older RDP implementations
> - Exposed RDP on the internet = one of the top ransomware entry points in real incidents
