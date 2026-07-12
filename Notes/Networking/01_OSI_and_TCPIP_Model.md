---
tags: [networking, cybersecurity, osi, cheatsheet]
---

# 01 — OSI Model & TCP/IP Model

---

## OSI Model (7 Layers)

> [!tip] Mnemonic — top to bottom
> **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way
> (Physical, Data Link, Network, Transport, Session, Presentation, Application)

| # | Layer | Protocol/Unit | What it does | Attack examples |
|---|---|---|---|---|
| 7 | **Application** | HTTP, DNS, FTP, SMTP / Data | User-facing services | SQL injection, XSS, phishing |
| 6 | **Presentation** | SSL/TLS, encoding / Data | Encryption, encoding, compression | SSL stripping, encoding attacks |
| 5 | **Session** | NetBIOS, RPC / Data | Opens/manages/closes sessions | Session hijacking |
| 4 | **Transport** | TCP, UDP / Segment | End-to-end delivery, ports | SYN flood, port scanning |
| 3 | **Network** | IP, ICMP, ARP / Packet | Routing between networks | IP spoofing, MITM |
| 2 | **Data Link** | Ethernet, MAC / Frame | Node-to-node on same network | ARP spoofing, MAC spoofing |
| 1 | **Physical** | Cables, signals / Bits | Raw bit transmission | Wiretapping, jamming |

---

## TCP/IP Model (4 Layers)

Maps to OSI but more practical — this is what actually runs the internet.

| TCP/IP Layer | Maps to OSI | Protocols |
|---|---|---|
| **Application** | Layers 5, 6, 7 | HTTP, HTTPS, DNS, FTP, SSH, SMTP, SNMP |
| **Transport** | Layer 4 | TCP, UDP |
| **Internet** | Layer 3 | IP, ICMP, ARP |
| **Network Access** | Layers 1, 2 | Ethernet, Wi-Fi, MAC |

---

## TCP vs UDP

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented (3-way handshake) | Connectionless |
| Reliability | Guaranteed delivery, ordered | No guarantees |
| Speed | Slower | Faster |
| Use cases | HTTP, SSH, FTP, SMTP | DNS, VoIP, video streaming |
| Security note | SYN flood targets TCP handshake | UDP flood, DNS amplification |

---

## The TCP 3-Way Handshake

```
Client          Server
  |--- SYN ------->|    "I want to connect"
  |<-- SYN-ACK ----|    "OK, I'm ready"
  |--- ACK ------->|    "Great, connection open"
```

> [!note] Security relevance
> A **SYN flood attack** sends thousands of SYN packets but never completes the handshake, exhausting the server's connection table. This is a classic DoS technique.

---

## TCP Flags (important for Nmap & Wireshark)

| Flag | Code | Meaning |
|---|---|---|
| SYN | `S` | Start connection |
| ACK | `A` | Acknowledge |
| FIN | `F` | Close connection |
| RST | `R` | Abort/reset connection |
| PSH | `P` | Push data immediately |
| URG | `U` | Urgent data |
| NULL | (none) | No flags — used in stealth scans |

---

## Where Attacks Live (by layer)

```
Layer 7 (App)     ← SQLi, XSS, phishing, CSRF, credential stuffing
Layer 6 (Pres)    ← SSL stripping
Layer 5 (Session) ← Session hijacking, cookie theft
Layer 4 (Trans)   ← SYN flood, port scanning, TCP hijacking
Layer 3 (Net)     ← IP spoofing, routing attacks, ICMP abuse
Layer 2 (Data)    ← ARP poisoning/spoofing, MAC flooding
Layer 1 (Phys)    ← Physical wiretapping, signal jamming
```

Knowing the layer helps you understand **what tool** to use and **where in the traffic** to look.
