---
tags: [networking, cybersecurity, cheatsheet, index]
---

# 🌐 Networking for Cybersecurity — Index

> [!info] How to use this
> Each file covers one topic independently. Start from the top if you're new; jump around if you need a quick reference.

---

## Files

| # | Topic | What it covers |
|---|---|---|
| 01 | [[01_OSI_and_TCPIP_Model]] | Layers, what each does, where attacks happen |
| 02 | [[02_Protocols]] | HTTP/S, DNS, FTP, SSH, SMTP, ARP, ICMP and more |
| 03 | [[03_IP_Addressing_and_Subnetting]] | IPv4, CIDR, subnetting, private vs public ranges |
| 04 | [[04_Ports_and_Services]] | Common ports, dangerous services, quick reference table |
| 05 | [[05_Nmap_and_Recon]] | Scanning types, flags, output formats, detection evasion |
| 06 | [[06_Packet_Analysis]] | Wireshark + tcpdump filters, what to look for |
| 07 | [[07_Network_Attacks]] | MITM, ARP spoofing, DNS poisoning, DoS, sniffing, etc. |
| 08 | [[08_Firewalls_IDS_IPS]] | Concepts, types, evasion basics |
| 09 | [[09_Wireless_Security]] | WPA2/3, WPS, attack types, key terms |

---

## Quick "What Do I Need?" Guide

| Situation | Go to |
|---|---|
| Box has unknown open ports | [[04_Ports_and_Services]] + [[05_Nmap_and_Recon]] |
| Need to scan a target | [[05_Nmap_and_Recon]] |
| Intercepting/reading traffic | [[06_Packet_Analysis]] |
| CTF has a packet capture (.pcap) | [[06_Packet_Analysis]] |
| Question about HTTP, DNS, FTP | [[02_Protocols]] |
| Need to understand an attack type | [[07_Network_Attacks]] |
| Subnetting question in exam | [[03_IP_Addressing_and_Subnetting]] |
| Wondering what layer something is on | [[01_OSI_and_TCPIP_Model]] |
