---
tags: [networking, cybersecurity, firewall, ids, ips, cheatsheet]
---

# 10 — Firewalls, IDS & IPS

---

## Firewalls

**What:** Controls traffic in/out of a network or host based on defined rules.

### Types

| Type | How it works | Example |
|---|---|---|
| **Packet filter** | Checks source/dest IP, port, protocol. No context. | Basic iptables rules |
| **Stateful firewall** | Tracks connection state — knows if packet belongs to an established session | Most modern firewalls |
| **Application firewall (WAF)** | Inspects Layer 7 — understands HTTP, can detect SQLi/XSS | Cloudflare WAF, ModSecurity |
| **Next-Gen Firewall (NGFW)** | Stateful + app awareness + user identity + IPS built in | Palo Alto, Fortinet |

### iptables (Linux firewall — you'll see this constantly)

```bash
# View current rules
iptables -L -v -n

# Allow established/related connections (always add this)
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow incoming SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP/HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Drop everything else
iptables -A INPUT -j DROP

# Delete a rule
iptables -D INPUT -p tcp --dport 80 -j ACCEPT

# Flush all rules (wipe everything)
iptables -F
```

### nftables (modern replacement for iptables)

```bash
nft list ruleset             # view current rules
nft add rule inet filter input tcp dport 22 accept
```

### UFW (uncomplicated firewall — Ubuntu/Debian wrapper)

```bash
ufw enable
ufw allow 22
ufw allow 80/tcp
ufw deny 3306
ufw status verbose
```

---

## IDS — Intrusion Detection System

**What:** Monitors network/host traffic and **alerts** when it sees suspicious activity. Does **not** block — only notifies.

| Type | What it monitors |
|---|---|
| **NIDS (Network IDS)** | Traffic on the network |
| **HIDS (Host IDS)** | Activity on a single host (files, processes, logs) |

**Detection methods:**

| Method | How | Weakness |
|---|---|---|
| **Signature-based** | Matches traffic against known attack patterns | Misses new/zero-day attacks |
| **Anomaly-based** | Learns what's "normal", alerts on deviations | High false positive rate |
| **Heuristic** | Behavioral analysis | More sophisticated, heavier |

**Popular tools:**
- **Snort** — most widely used open-source NIDS, signature-based
- **Suricata** — multi-threaded, can also do IPS
- **Zeek (Bro)** — network analysis framework, great for logging

---

## IPS — Intrusion Prevention System

**What:** Like an IDS but **actively blocks** suspicious traffic in real time.

**IDS vs IPS:**
```
IDS: Monitor → Detect → Alert
IPS: Monitor → Detect → Block (inline)
```

An IPS sits inline in the traffic path; an IDS passively watches a copy of traffic (via port mirroring/TAP).

---

## Common Firewall Evasion Techniques (attacker perspective)

Know these so you can detect them in logs/traffic:

| Technique | How it works |
|---|---|
| **Packet fragmentation** | Split a packet into fragments; some firewalls don't reassemble before inspecting |
| **Using allowed ports** | Put malicious traffic on port 80/443 — often allowed through |
| **Protocol tunneling** | Tunnel traffic inside allowed protocols (HTTP, DNS, ICMP) |
| **Low and slow** | Spread scan/attack over long time — avoids rate-based detection |
| **Source IP spoofing** | Forge source IP (harder to do for TCP due to 3-way handshake) |
| **Decoy scanning** | Nmap `-D RND:10` — sends scan from fake IPs alongside real ones |
| **NULL/FIN/Xmas scans** | Bypass packet-filter firewalls that only look at SYN packets |

**Nmap evasion flags:**
```bash
nmap -f target                    # fragment packets
nmap -D RND:10 target              # decoy scan (10 random fake IPs)
nmap --source-port 53 target        # spoof source port 53 (DNS — often allowed through)
nmap -T1 --randomize-hosts target    # slow, random order
nmap --data-length 25 target          # add random data to packets (confuse fingerprinting)
```

---

## DMZ (Demilitarized Zone)

A network segment between the internet and the internal network, where public-facing servers live.

```
Internet
   |
[Firewall]
   |
  DMZ (web server, mail server, DNS)
   |
[Firewall]
   |
Internal LAN (workstations, databases, sensitive systems)
```

**Why it matters:** If an attacker compromises a web server in the DMZ, they're still behind another firewall from the internal network. Lateral movement becomes harder.

---

## Key Concepts Summary

| Concept | One-liner |
|---|---|
| Firewall | Allow/deny traffic based on rules |
| IDS | Watch and alert — does NOT block |
| IPS | Watch, alert, AND block (inline) |
| WAF | Application-layer firewall — understands HTTP |
| NGFW | Stateful + IPS + app awareness in one box |
| DMZ | Segmented zone for public-facing services |
| Signature detection | Match against known bad patterns |
| Anomaly detection | Flag deviations from normal baseline |
| Defense in depth | Layered security — no single point of failure |

---

## Checking What's Listening on Your System

```bash
ss -tuln                          # modern tool — listening ports
netstat -tuln                      # older alternative
ss -tulnp                           # includes which process is listening
lsof -i :80                          # what's using port 80
```

This is useful both for hardening your own system (close what's unnecessary) and for understanding a target once you have access.
