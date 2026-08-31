---
tags: [networking, cybersecurity, ip, mac, subnetting, cheatsheet]
---

# 02 — IP Addressing, MAC Addresses & Subnetting

---

## IP Addresses — Why They Matter for Security

An IP address is a unique numerical label assigned to every device on a network. From a cybersecurity standpoint, IP addresses are the primary way attackers locate, target, and track devices. Knowing your IP address topology is fundamental to understanding your attack surface.

**Key security notes:**
- IP addresses can be spoofed (IP spoofing) to forge the source of a packet
- Public IPs are exposed to the internet; private IPs sit behind NAT
- Attackers use tools like `nmap` to scan IP ranges and discover open services
- Logging IPs is essential for forensics and incident response

---

## IPv4 Basics

- 32-bit address written as 4 octets: `192.168.1.100`
- Each octet = 8 bits, range 0–255
- Two parts: **Network** portion + **Host** portion (split determined by subnet mask)

## IPv4 vs IPv6

| | IPv4 | IPv6 |
|---|---|---|
| Address space | ~4.2 billion | 340 undecillion |
| Header complexity | Simple | More complex |
| NAT required? | Yes (hides devices) | No (every device gets a public IP) |
| Attack surface | Smaller per device | Larger — every device directly reachable |
| Weakness | IP spoofing, scanning | IPv6 misconfiguration, rogue RAs |

### IPv6 Basics

128-bit address written as 8 groups of 4 hex digits:
`2001:0db8:85a3:0000:0000:8a2e:0370:7334`

Shorthand rules:
- Leading zeros in a group can be dropped: `0db8` → `db8`
- One consecutive group of all zeros can be replaced with `::`: `2001:db8::1`

| Type | Example | Equivalent to IPv4 |
|---|---|---|
| Loopback | `::1` | 127.0.0.1 |
| Link-local | `fe80::/10` | 169.254.x.x |
| Global unicast | `2000::/3` | Public IP |
| Multicast | `ff00::/8` | 224.x.x.x |

---

## IPv4 Address Classes (mostly legacy but still tested)

| Class | Range | Default Mask | Hosts per Network |
|---|---|---|---|
| A | 1.0.0.0 – 126.255.255.255 | /8 (255.0.0.0) | ~16 million |
| B | 128.0.0.0 – 191.255.255.255 | /16 (255.255.0.0) | ~65,000 |
| C | 192.0.0.0 – 223.255.255.255 | /24 (255.255.255.0) | 254 |
| D | 224.0.0.0 – 239.255.255.255 | — | Multicast |
| E | 240.0.0.0 – 255.255.255.255 | — | Reserved/Research |

---

## Private IP Ranges (RFC 1918)

These are **non-routable on the internet** — used inside LANs. If you see these during a scan, you're looking at an internal network.

| Range | CIDR | Class |
|---|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | A |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | B |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | C |

**Other special ranges:**

| Address | Purpose |
|---|---|
| 127.0.0.1 | Loopback (localhost) |
| 0.0.0.0 | Unspecified / all interfaces |
| 255.255.255.255 | Broadcast (all hosts) |
| 169.254.x.x | APIPA / link-local (DHCP failed) |

---

## CIDR Notation

CIDR = Classless Inter-Domain Routing. The `/24` in `192.168.1.0/24` tells you how many bits are the network portion.

### CIDR Quick Reference Table

| CIDR | Subnet Mask | Hosts | Typical use |
|---|---|---|---|
| /8 | 255.0.0.0 | 16,777,214 | Large corp / ISP |
| /16 | 255.255.0.0 | 65,534 | Medium org |
| /24 | 255.255.255.0 | 254 | Home/small office LAN |
| /25 | 255.255.255.128 | 126 | Half of a /24 |
| /26 | 255.255.255.192 | 62 | |
| /27 | 255.255.255.224 | 30 | |
| /28 | 255.255.255.240 | 14 | Small VLAN |
| /29 | 255.255.255.248 | 6 | Point-to-point links |
| /30 | 255.255.255.252 | 2 | Router links |
| /32 | 255.255.255.255 | 1 (host only) | Single host route |

> [!tip] Formula
> **Hosts = 2^(32 - CIDR) - 2**
> Subtract 2 for network address (first IP) and broadcast address (last IP).

---

## Subnetting — Step by Step

**Example: 192.168.1.0/26**

1. **Hosts available:** 2^(32-26) - 2 = 2^6 - 2 = 62 hosts
2. **Subnet mask:** /26 = 255.255.255.192
3. **Block size:** 256 - 192 = **64**
4. **Subnets of a /24:**
   - 192.168.1.0 – 192.168.1.63 (network: .0, broadcast: .63)
   - 192.168.1.64 – 192.168.1.127 (network: .64, broadcast: .127)
   - 192.168.1.128 – 192.168.1.191
   - 192.168.1.192 – 192.168.1.255

> [!tip] Quick subnet mask → binary trick
> /24 = 11111111.11111111.11111111.00000000
> /26 = 11111111.11111111.11111111.11000000
> Count the 1s = CIDR prefix. 0s = host bits.

---

## Key Addresses in any Subnet

Given `192.168.1.0/24`:
- **Network address:** `192.168.1.0` — identifies the subnet, not assigned to a host
- **First usable host:** `192.168.1.1`
- **Last usable host:** `192.168.1.254`
- **Broadcast address:** `192.168.1.255` — sends to all hosts in subnet

---

## MAC Addresses

A MAC (Media Access Control) address is a 48-bit hardware identifier burned into a network interface card (NIC). Format: `AA:BB:CC:DD:EE:FF`. The first 3 bytes identify the manufacturer (OUI), the last 3 are unique to the device.

**Security implications:**
- MAC addresses only travel within a local network segment — routers strip them
- **MAC spoofing:** attackers change their MAC to bypass MAC filtering on Wi-Fi or switches
- **ARP poisoning:** an attacker links their MAC to another device's IP, intercepting traffic (man-in-the-middle) — see [[05_Core_Protocols]] and [[09_Network_Attacks]]
- MAC addresses appear in Wi-Fi probe requests — used to track people's physical location
- Modern OSes (iOS, Android, Windows 11) now randomize MACs for privacy

---

## Subnetting — Why It Matters for Security

- Subnetting divides a large IP network into smaller logical networks (subnets), improving performance, security, and manageability.
- Typical benefits: each department/zone gets its own subnet, inter-subnet traffic is routed through a router, and broadcast traffic stays contained to each subnet.

> [!warning] Why subnetting matters for security
> - **Scanning scope:** `nmap 192.168.1.0/24` — knowing the subnet tells you exactly what range to scan
> - **Segmentation:** Networks are split into subnets to isolate sensitive systems (DMZ, production, dev)
> - **Pivoting:** After getting a foothold on a box, `ifconfig` shows you what other subnets it's connected to — those become new targets
> - **Private IP in a public context:** If you find a private IP in HTTP headers or DNS records, you've found internal network topology → info leak

---

## Useful Commands

```bash
ip a                           # show interfaces + IPs (Linux)
ifconfig                        # older equivalent
ip route                         # routing table
ip route show                     # see what goes where
nmap -sn 192.168.1.0/24           # ping sweep — discover live hosts on subnet
ipcalc 192.168.1.0/26             # calculate subnet details (pkg install ipcalc)
```
