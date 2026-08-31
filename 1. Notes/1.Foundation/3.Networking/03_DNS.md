---
tags: [networking, cybersecurity, dns, cheatsheet]
---

# 03 — DNS (Domain Name System)

Port 53 (UDP/TCP). DNS translates human-readable names (`google.com`) into IP addresses (`142.250.80.46`) — no DNS, no browsing by name.

---

## What is DNS?

Much like every house has a unique address for mail, every computer on the internet has a unique IP address (e.g. `104.26.10.229`). Remembering that is inconvenient, so DNS lets you use `tryhackme.com` instead.

---

## Domain Hierarchy

### TLD (Top-Level Domain)
The right-most part of a domain name — e.g. `.com` in `tryhackme.com`.
- **gTLD** (Generic): originally purpose-based — `.com` commercial, `.org` organization, `.edu` education, `.gov` government. Now hugely expanded (`.online`, `.club`, `.website`, `.biz`, etc.) — [full IANA TLD list](https://data.iana.org/TLD/tlds-alpha-by-domain.txt).
- **ccTLD** (Country Code): geography-based — `.ca` Canada, `.co.uk` United Kingdom, etc.

### Second-Level Domain
In `tryhackme.com`, `tryhackme` is the second-level domain. Limited to 63 characters + TLD; only `a-z`, `0-9`, and hyphens (can't start/end with a hyphen or have consecutive hyphens).

### Subdomain
Sits left of the second-level domain, separated by a period — e.g. `admin` in `admin.tryhackme.com`. Same character rules as above. You can chain multiple subdomains (`jupiter.servers.tryhackme.com`), with a total length limit of 253 characters. No limit on the number of subdomains per domain.

---

## DNS Record Types

| Record | Purpose | Example |
|---|---|---|
| **A** | Domain → IPv4 | `google.com → 142.250.x.x` |
| **AAAA** | Domain → IPv6 | `2606:4700:20::681a:be5` |
| **CNAME** | Alias for another domain | `store.tryhackme.com → shops.shopify.com` (a further lookup resolves the IP) |
| **MX** | Mail server(s) for the domain, with a priority flag for failover order | `alt1.aspmx.l.google.com` |
| **TXT** | Arbitrary text — SPF, DKIM/DMARC, domain-ownership verification | see below |
| **NS** | Nameservers (authoritative servers) for a domain | `kip.ns.cloudflare.com` |
| **PTR** | Reverse DNS — IP → domain | |

**TXT record examples:**
```
_acme-challenge.example.com TXT "token_value_here"
@ TXT "v=spf1 ip4:192.0.2.0/24 include:_spf.google.com include:amazonses.com ~all"
_dmarc.example.com TXT "v=DMARC1; p=reject; rua=mailto:dmarc-reports@example.com; adkim=s; aspf=s; pct=100"
@ TXT "MS=ms12345678"
```

---

## How a DNS Request Actually Resolves

1. Your computer checks its **local cache** first. If found, done.
2. If not cached, it asks a **Recursive DNS Server** (usually your ISP's, or a custom one like 1.1.1.1/8.8.8.8). This server has its own cache — if it has the answer, it replies immediately (common for popular sites).
3. If not cached there either, the recursive server queries a **root DNS server**, which redirects it to the correct **TLD server** based on the domain's TLD (e.g. `.com`).
4. The TLD server points to the **authoritative nameserver** for the specific domain (e.g. `tryhackme.com`'s nameservers are `kip.ns.cloudflare.com` and `uma.ns.cloudflare.com` — often multiple, for redundancy).
5. The **authoritative server** returns the actual DNS record. This gets cached at the recursive server (per the record's **TTL**, in seconds) and relayed back to your computer.

```
Client → Local cache → Recursive resolver → Root server → TLD server → Authoritative server → (answer flows back, caching along the way)
```

---

## DNS Commands

```bash
dig domain.com               # full DNS query
dig domain.com MX             # specific record type
dig @8.8.8.8 domain.com       # query a specific DNS server
nslookup domain.com             # simpler alternative
host domain.com                  # quick lookup
dig axfr @ns.target.com target.com   # attempt a zone transfer (dumps the whole zone if misconfigured)
```

---

## DNS Security Threats

| Threat | What it is |
|---|---|
| **DNS cache poisoning / spoofing** | Attacker injects forged records so a resolver (or victim) gets a malicious IP for a legitimate domain |
| **DNS tunneling** | Data exfiltration hidden inside DNS queries — hard to detect, look for long/base64-looking subdomains |
| **DNS amplification DDoS** | Small spoofed queries trigger large responses sent to a victim, flooding them |
| **Typosquatting** | Registering lookalike domains (`gooogle.com`) to catch typos/phish users |
| **DNS hijacking** | Malware changes a router/device's configured DNS server to an attacker-controlled one |
| **Zone transfer misconfiguration** | If `AXFR` isn't restricted, anyone can dump the entire DNS zone — subdomains, internal names, mail servers |

> [!note] Why this matters for recon
> DNS enumeration (subdomains, MX records, TXT records) is one of the first things to check on a new target — see [[07_Nmap_and_Recon]] for tools like `dnsenum`, `dnsrecon`, and `sublist3r`.

**Defenses:** DNSSEC (cryptographically signs records), DNS over HTTPS (DoH), DNS over TLS (DoT), restricting zone transfers to trusted IPs only.
