---
tags: [networking, cybersecurity, attacks, cheatsheet]
---

# 07 — Network Attacks

> [!warning] All of the below is for understanding, defense, and authorized testing only. Know the attacks so you can detect, prevent, and defend against them.

---

## Man-in-the-Middle (MITM)

**What:** Attacker secretly intercepts and potentially modifies traffic between two parties who believe they're communicating directly.

```
Normal:    Alice ←————————→ Bob
MITM:      Alice ←—→ Attacker ←—→ Bob
```

**How attackers achieve MITM position:**
- ARP spoofing (on local network)
- Rogue WiFi access point
- DNS poisoning
- BGP hijacking (ISP level)

**What they can do once in position:**
- Read plaintext traffic (HTTP, FTP, Telnet)
- Steal session cookies / credentials
- Inject malicious content into HTTP responses
- SSL stripping (downgrade HTTPS → HTTP)

**Detection:**
- Duplicate ARP entries in ARP cache
- TLS certificate warnings in browser
- Unexpected latency

---

## ARP Spoofing / ARP Poisoning

**What:** Attacker sends fake ARP replies to associate their MAC with another device's IP, redirecting traffic through themselves.

```
Target thinks: 192.168.1.1 (gateway) → Attacker's MAC
Traffic now flows through attacker instead of the router
```

**How to check your ARP cache:**
```bash
arp -a / arp -n        # see all ARP entries
ip neigh               # Linux alternative
```

**What to look for:** Two different IPs mapped to the same MAC address is a red flag.

**Tools used by attackers:** `arpspoof`, `ettercap`, `bettercap`

**Defense:** Dynamic ARP Inspection (DAI) on managed switches, static ARP entries for critical hosts, HTTPS everywhere.

---

## DNS Spoofing / DNS Cache Poisoning

**What:** Attacker injects false DNS records, so when a victim looks up `bank.com`, they get the attacker's IP instead of the real one.

```
Victim:   "What's the IP for bank.com?"
DNS:       "192.168.1.99" ← (attacker's server, not the real bank)
Victim:   Connects to attacker's fake site
```

**Two variants:**
- **Cache poisoning:** Corrupt the DNS cache of a resolver serving many users — one successful attack affects everyone using that resolver
- **Local DNS spoofing:** On a network where attacker is already doing MITM

**Defense:** DNSSEC, DNS over HTTPS (DoH), DNS over TLS (DoT).

---

## DoS & DDoS

**DoS (Denial of Service):** One attacker overwhelms a target, making it unavailable.
**DDoS (Distributed DoS):** Same goal but from many sources (botnet) — much harder to block.

### Common DoS Techniques

| Attack | How it works | Layer |
|---|---|---|
| **SYN Flood** | Sends thousands of SYN packets, never completes handshake — exhausts connection table | L4 |
| **UDP Flood** | Floods target with UDP packets to random ports | L4 |
| **ICMP Flood (Ping Flood)** | Overwhelms target with ICMP echo requests | L3 |
| **HTTP Flood** | Floods web server with legitimate-looking HTTP GET/POST requests | L7 |
| **Slowloris** | Keeps many HTTP connections open but sends data very slowly — exhausts connection pool | L7 |
| **Amplification (DNS/NTP)** | Sends small request to a public server spoofing victim's IP — server sends large response to victim | L3/L4 |

> [!note] Amplification explained
> DNS response can be 50x larger than the request. Attacker spoofs victim's IP → sends tiny DNS queries to many public resolvers → they all send large responses to the victim → victim flooded with traffic from "legitimate" servers.

---

## Password Attacks

| Type | What it is | Tool |
|---|---|---|
| **Brute force** | Try every possible combination | Hydra, Hashcat |
| **Dictionary attack** | Try words from a wordlist | Hydra, John the Ripper |
| **Credential stuffing** | Use leaked username:password pairs from data breaches | Custom scripts |
| **Password spraying** | Try one common password against many accounts | Spray |
| **Rainbow table** | Precomputed hash → password lookup (offline) | Hashcat, RainbowCrack |

**Common wordlists:**
- `rockyou.txt` — most famous, 14M passwords from 2009 breach — on most Kali/security distros
- `SecLists` — massive collection maintained on GitHub

**Hydra quick reference:**
```bash
hydra -l username -P wordlist.txt ssh://target
hydra -L users.txt -P pass.txt ftp://target
hydra -l admin -P wordlist.txt http-post-form "/login:user=^USER^&pass=^PASS^:F=incorrect"
```

---

## Packet Sniffing

**What:** Capturing network traffic to read contents — works on unencrypted protocols.

**What's visible in plaintext:**
- HTTP: full URLs, cookies, POST bodies (passwords in login forms)
- FTP: username + password
- Telnet: everything typed (including passwords)
- POP3/IMAP without TLS: email credentials

**Defense:** TLS/HTTPS everywhere, avoid plaintext protocols, use VPN on untrusted networks.

---

## Port Scanning (from the attacker's view)

Not destructive, but used for reconnaissance. Reveals:
- What OS is running
- What services/versions are exposed
- Potential attack surface

Defenders look for: unusual scan patterns in logs (many ports hit in sequence, short timeframes from one IP).

**IDS evasion techniques attackers use:**
- Slow scans (`-T1` or `-T0`)
- Fragmented packets (`-f`)
- Decoy scans (`-D RND:10` — generates fake source IPs)
- Randomized port order (`--randomize-hosts`)

---

## Session Hijacking

**What:** Stealing or forging a session token to impersonate an authenticated user without needing their password.

**How:**
- Steal session cookie from unencrypted HTTP traffic (Wireshark)
- XSS attack that reads `document.cookie`
- Predictable session IDs — brute force

**Defense:** HttpOnly + Secure flags on cookies, HTTPS everywhere, short session timeouts.

---

## SSL Stripping

**What:** Downgrades a HTTPS connection to HTTP so traffic can be read.

**How it works:**
1. Attacker is in MITM position
2. Victim requests `http://bank.com`
3. Attacker forwards request to real `https://bank.com`
4. Attacker receives encrypted response from bank, strips TLS, sends **plaintext HTTP** back to victim
5. Victim thinks they're on HTTP (no padlock), attacker reads everything

**Defense:** HSTS (HTTP Strict Transport Security) — browser remembers "this site must be HTTPS" and refuses HTTP.

---

## Reconnaissance Attacks

| Technique | What it reveals |
|---|---|
| Ping sweep | Which hosts are alive |
| Port scan | Which services are running |
| Banner grabbing | Software versions → known CVEs |
| DNS enumeration | Subdomains, mail servers, internal names |
| WHOIS lookup | Registrant info, nameservers |
| Google dorking | Exposed files, login pages, error messages via search |
| OSINT | Email addresses, employee names, tech stack from public info |

**Google dork examples:**
```
site:target.com filetype:pdf
site:target.com intitle:"index of"
site:target.com inurl:admin
"target.com" filetype:xls
```

---

## Attack Summary Map

```
Reconnaissance  →  nmap, whois, DNS enum, OSINT
Gaining Access  →  Exploit open ports, brute force, phishing, MITM
Persistence     →  Backdoor, SSH key injection, cron job
Lateral Move    →  Pivot to other subnets, credential reuse
Exfiltration    →  DNS tunneling, HTTP, ICMP covert channels
Covering Tracks →  Clear logs, timestomping
```
