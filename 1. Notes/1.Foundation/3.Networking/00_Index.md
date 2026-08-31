---
tags: [networking, cybersecurity, cheatsheet, index]
---

# 🌐 Networking for Cybersecurity — Index

> [!info] How to use this
> Each file covers one topic independently. Files 01–05 are **foundations** (how networking works). Files 06–11 are **security-focused** (how it's attacked/defended/analyzed). Start from the top if you're new; jump around if you need a quick reference.

---

## Foundations

| # | Topic | What it covers |
|---|---|---|
| 01 | [[01_OSI_and_TCPIP_Model]] | Layers, what each does, where attacks happen |
| 02 | [[02_IP_Addressing_MAC_and_Subnetting]] | IPv4/IPv6, MAC addresses, CIDR, subnetting, private vs public ranges |
| 03 | [[03_DNS]] | Domain hierarchy, record types, resolution flow, DNS threats |
| 04 | [[04_HTTP_and_HTTPS]] | URLs, methods, requests/responses, status codes |
| 05 | [[05_Core_Protocols]] | FTP, SSH, SMTP, ARP, DHCP, ICMP, SNMP, SMB, RDP, Telnet, Encapsulation |

## Security & Offense

| # | Topic | What it covers |
|---|---|---|
| 06 | [[06_Ports_and_Services]] | Common ports, dangerous services, quick reference table |
| 07 | [[07_Nmap_and_Recon]] | Scanning types, flags, output formats, detection evasion |
| 08 | [[08_Packet_Analysis]] | Wireshark + tcpdump filters, what to look for |
| 09 | [[09_Network_Attacks]] | MITM, ARP spoofing, DNS poisoning, DoS, sniffing, etc. |
| 10 | [[10_Firewalls_IDS_IPS]] | Concepts, types, evasion basics |
| 11 | [[11_Wireless_Security]] | WPA2/3, WPS, attack types, key terms |

> [!note] CIA Triad
> Your CIA Triad note (Confidentiality, Integrity, Availability) is general security theory, not networking-specific — it's cleaner to keep it in a separate **Security Fundamentals** folder rather than this one. Let me know if you want it moved/rebuilt there.

---

## Quick "What Do I Need?" Guide

| Situation | Go to |
|---|---|
| Box has unknown open ports | [[06_Ports_and_Services]] + [[07_Nmap_and_Recon]] |
| Need to scan a target | [[07_Nmap_and_Recon]] |
| Intercepting/reading traffic | [[08_Packet_Analysis]] |
| CTF has a packet capture (.pcap) | [[08_Packet_Analysis]] |
| Question about HTTP, FTP, SSH, ARP, DHCP | [[05_Core_Protocols]] |
| Question about a URL, request, or status code | [[04_HTTP_and_HTTPS]] |
| Question about domains/subdomains/DNS records | [[03_DNS]] |
| Need to understand an attack type | [[09_Network_Attacks]] |
| Subnetting or MAC address question | [[02_IP_Addressing_MAC_and_Subnetting]] |
| Wondering what layer something is on | [[01_OSI_and_TCPIP_Model]] |
