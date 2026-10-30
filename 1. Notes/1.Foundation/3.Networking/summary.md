---
tags: [networking, cybersecurity, summary, cheatsheet]
---

# 🌐 Network Fundamentals — Summary

> [!info] What this is
> A quick overview of how networks work, the way TryHackMe would teach it: **what each thing is** + **how it works**, one block per topic. Each section links to the full note in this folder when you want the deep dive.

**Networking = computers talking to each other.** To do that, they need a shared language (protocols), addresses (IP/MAC), routes (routers), and rules about who may talk (firewalls). Almost every cyber attack happens *across* a network — so this is the foundation everything else sits on.

---

## 1. OSI Model — the 7 layers of talking

**What:** A conceptual framework that splits network communication into 7 layers, each with its own job. It's a *model*, not a physical thing — it helps you reason about where problems (and attacks) live.

**How it works:** Data travels **down** the stack on the sending side, each layer wrapping the last with its own header (encapsulation), then **up** the stack on the receiving side, each layer unwrapping its own header.

> [!tip] Mnemonic (top → bottom)
> **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

| # | Layer | Job | Who lives here |
|---|---|---|---|
| 7 | Application | User-facing services | HTTP, DNS, FTP, SMTP |
| 6 | Presentation | Encryption, encoding | SSL/TLS |
| 5 | Session | Manage connections | NetBIOS, RPC |
| 4 | Transport | End-to-end delivery + ports | TCP, UDP |
| 3 | Network | Routing between networks | IP, ICMP, ARP |
| 2 | Data Link | Delivery on the same network | Ethernet, MAC |
| 1 | Physical | Raw bits on the wire | Cables, signals |

📘 Full breakdown → [[01_OSI_and_TCPIP_Model]]

---

## 2. TCP/IP — the 4 layers that actually run the internet

**What:** The OSI model's practical sibling — the model real networks use. It collapses OSI's 7 layers into 4.

**How it works:** Everything on the internet is a **packet** with headers telling routers where it's going (IP) and apps which program it belongs to (port). TCP/IP is the plumbing that moves it.

| TCP/IP Layer | ≈ OSI | Protocols |
|---|---|---|
| Application | 5+6+7 | HTTP, DNS, SSH, SMTP |
| Transport | 4 | TCP, UDP |
| Internet | 3 | IP, ICMP, ARP |
| Network Access | 1+2 | Ethernet, Wi-Fi, MAC |

### TCP vs UDP — reliability vs speed

| | TCP | UDP |
|---|---|---|
| Connection | Yes (3-way handshake) | No |
| Delivery | Guaranteed, ordered | Best-effort |
| Use cases | HTTP, SSH, FTP, SMTP | DNS, VoIP, video |
| Attack angle | SYN flood | Amplification |

**The 3-way handshake** (`SYN → SYN-ACK → ACK`) is how TCP opens a connection — and the target of SYN-flood DoS attacks.

📘 Full breakdown → [[01_OSI_and_TCPIP_Model]]

---

## 3. DNS — the internet's phonebook

**What:** Translates human-readable names (`tryhackme.com`) into IP addresses (`104.26.10.229`). Port **53**.

**How it works:** Your computer asks a **recursive resolver** (usually your ISP's) for a name. If it's not cached, the resolver walks the chain: **root** → **TLD** server (`.com`) → **authoritative** server for that domain → the actual record, which gets cached along the way (per its **TTL**).

```
Client → Cache → Recursive resolver → Root → TLD → Authoritative → answer flows back
```

**Attack angle:** DNS cache poisoning, DNS tunneling (exfil hidden in queries), amplification DDoS, zone-transfer misconfig (anyone can `dig axfr` the whole domain).

📘 Full breakdown → [[03_DNS]]

---

## 4. HTTP & HTTPS — web traffic

**What:** HTTP (port **80**) is the plaintext ruleset for loading web pages. HTTPS (port **443**) is HTTP wrapped in **TLS/SSL encryption** — stops sniffing and confirms the server is really who it claims to be.

**How it works:** A client sends a **request** (`GET / HTTP/1.1` + headers → host, user-agent…), the server replies with a **status code** + body. The request/response is just text — which is why web attacks (SQLi, XSS) focus here, and why anything sensitive needs HTTPS.

**Status codes to know:** 200 OK · 301/302 redirect · 401 not authorised · 403 forbidden · 404 not found · 500 server error.

> [!note] Security
> Plain HTTP = everything (cookies, POST bodies, URLs) sniffable on the network. HTTPS stops that, but app-layer attacks still work.

📘 Full breakdown → [[04_HTTP_and_HTTPS]]

---

## 5. Core Protocols — the other apps on the wire

**What:** The protocols you'll meet constantly in CTFs and pentests. **A protocol is just a set of rules two devices agree on to talk.**

**How it works:** Each service listens on its own port — connect to the port, speak the protocol.

| Protocol | Port | What it is | Why it matters |
|---|---|---|---|
| **FTP** | 21/20 | File transfer | Plaintext creds, anonymous login |
| **SSH** | 22 | Encrypted remote shell | Your primary remote-admin tool |
| **Telnet** | 23 | Plaintext remote shell | Nothing encrypted — banner grab with it |
| **SMTP** | 25/587 | Sending mail | Email spoofing, user enumeration |
| **POP3/IMAP** | 110/143 | Receiving mail | Plaintext on default ports |
| **ARP** | L2 | Maps IP → MAC on a LAN | Unauthenticated → ARP spoofing/MITM |
| **DHCP** | 67/68 | Auto-assigns IPs | Rogue DHCP server = malicious config |
| **ICMP** | L3 | Ping/traceroute diagnostics | Ping sweeps, ICMP tunneling |
| **SNMP** | 161/162 | Device management | Default community strings (`public`) |
| **SMB** | 445/139 | Windows file sharing | EternalBlue, null sessions |
| **RDP** | 3389 | Windows remote desktop | Brute force, BlueKeep |

📘 Full breakdown → [[05_Core_Protocols]]

---

## 6. DHCP — auto-assigning addresses

**What:** Hands out IP addresses (and gateway/DNS config) to devices when they join a network, so nobody configures them by hand.

**How it works:** The **DORA** handshake:

```
Discover  →  "Any DHCP server out there?"
Offer     →  "Here's an IP you can use."
Request   →  "I'll take it."
Acknowledge → "Done — it's yours."
```

**Attack angle:** A **rogue DHCP server** on the LAN can hand out a fake gateway/DNS, silently routing the victim's traffic through the attacker.

---

## 7. Firewalls, IDS & IPS — who's allowed in?

**What:** A firewall **allows/blocks traffic by rules**. It's the bouncer at the network's door.

**How it works:**
- **Packet filter** — checks source/dest IP, port, protocol. No context.
- **Stateful** — also tracks connection state (knows if a packet belongs to an established session). Most modern firewalls.
- **WAF** — understands HTTP, blocks SQLi/XSS at Layer 7.
- **NGFW** — stateful + app awareness + IPS built in.

| | Does it block? | Job |
|---|---|---|
| **Firewall** | ✅ allows/blocks by rules | Gatekeeper |
| **IDS** | ❌ alerts on suspicious traffic | Watchdog (Snort, Suricata) |
| **IPS** | ✅ alerts *and* blocks, inline | Active watchdog |

**Evasion to know:** fragmentation, tunneling inside allowed ports (80/443/DNS), null/FIN/Xmas scans, decoy sources (`nmap -D`).

📘 Full breakdown → [[10_Firewalls_IDS_IPS]]

---

## 8. Ports & Services — how one machine runs many apps

**What:** A port is a numbered "door" that lets traffic reach the right program on a machine (SSH owns 22, HTTP owns 80…). One IP, many services — the port picks which.

| Range | Name | Who uses it |
|---|---|---|
| 0–1023 | Well-known | Standard services (SSH, HTTP, FTP) |
| 1024–49151 | Registered | Apps (MySQL 3306, RDP 3389) |
| 49152–65535 | Dynamic | Client-side temporary connections |

**Why it matters:** An **open port = a service = an attack surface**. This is exactly what scanning (`nmap -sV target`) reveals first.

**Top ports you'll see:** 21 FTP · 22 SSH · 23 Telnet · 25 SMTP · 53 DNS · 80/443 HTTP/S · 110/143 mail · 445 SMB · 3306 MySQL · 3389 RDP · 8080 proxy/alt HTTP.

📘 Full table → [[06_Ports_and_Services]] · [[07_Nmap_and_Recon]]

---

## How it all fits together - one packet's journey

> [!example] You type `https://tryhackme.com`:
> 1. **DNS** resolves `tryhackme.com` → an IP.
> 2. TCP does the **3-way handshake** (SYN → SYN-ACK → ACK) to the server's port **443**.
> 3. Your browser sends an **HTTPS request** — handshaked and encrypted by TLS at the Transport/Session edge.
> 4. The request is wrapped into **segments → packets → frames** (encapsulation), routed hop by hop via **IP**.
> 5. At the server, the layers **un-stack**, the service on port 443 answers with a **200 OK**, and the page loads.

Every attack you'll study is somewhere in that chain: pre-wire (DNS, phishing), on the wire (spoofing, MITM), at a port (exploits), or at the app (SQLi/XSS). Depth-in-depth reading order → [[00_Index]].