---
tags: [networking, cybersecurity, ports, services, cheatsheet]
---

# 04 — Ports & Services

---

## Port Ranges

| Range | Name | Notes |
|---|---|---|
| 0 – 1023 | Well-known ports | Assigned to standard services (HTTP, SSH, FTP...) |
| 1024 – 49151 | Registered ports | Used by apps (MySQL 3306, RDP 3389...) |
| 49152 – 65535 | Dynamic/ephemeral ports | Assigned temporarily by OS for client connections |

---

## Must-Know Ports (Cybersecurity)

| Port | Protocol | Service | Notes |
|---|---|---|---|
| 20 | TCP | FTP Data | Plaintext file transfer — sniff credentials |
| 21 | TCP | FTP Control | Login in plaintext — brute force, anon login |
| 22 | TCP | SSH | Encrypted remote shell — brute force if weak password |
| 23 | TCP | Telnet | Fully plaintext SSH predecessor — almost never used but still found |
| 25 | TCP | SMTP | Mail sending — open relay = email spoofing |
| 53 | TCP/UDP | DNS | Zone transfer, DNS enum, DNS poisoning |
| 67/68 | UDP | DHCP | Rogue DHCP server attack |
| 69 | UDP | TFTP | Trivial FTP — no auth at all |
| 80 | TCP | HTTP | Web — SQLi, XSS, directory traversal |
| 110 | TCP | POP3 | Email retrieval — plaintext creds |
| 111 | TCP/UDP | RPCBind | NFS enumeration starting point |
| 119 | TCP | NNTP | News protocol — rarely used, sometimes forgotten/exposed |
| 135 | TCP | MS-RPC | Windows RPC — many exploits target this |
| 137-139 | TCP/UDP | NetBIOS | Windows name resolution, file sharing |
| 143 | TCP | IMAP | Email sync — plaintext creds on port 143 |
| 161/162 | UDP | SNMP | Device management — default community strings |
| 389 | TCP | LDAP | Directory service — user enumeration |
| 443 | TCP | HTTPS | Encrypted HTTP — still vulnerable to app-layer attacks |
| 445 | TCP | SMB | Windows file share — EternalBlue, null sessions |
| 465 | TCP | SMTPS | SMTP over SSL |
| 500 | UDP | IKE/IPSec | VPN — fingerprinting |
| 512-514 | TCP | RSH/Rlogin | Ancient remote shell — no auth sometimes |
| 587 | TCP | SMTP (submission) | Mail with auth — brute force |
| 631 | TCP | IPP (CUPS) | Printer — sometimes exposes info |
| 993 | TCP | IMAPS | IMAP over SSL |
| 995 | TCP | POP3S | POP3 over SSL |
| 1433 | TCP | MSSQL | Microsoft SQL Server — SA default creds |
| 1521 | TCP | Oracle DB | Oracle database |
| 2049 | TCP | NFS | Network file share — often misconfigured permissions |
| 3306 | TCP | MySQL | Database — brute force, SQL injection pivot |
| 3389 | TCP | RDP | Windows Remote Desktop — brute force, BlueKeep |
| 5432 | TCP | PostgreSQL | Database |
| 5900 | TCP | VNC | Remote desktop — often weak/no auth |
| 6379 | TCP | Redis | No auth by default in older versions — RCE possible |
| 8080 | TCP | HTTP Alt | Dev servers, proxy, Tomcat admin |
| 8443 | TCP | HTTPS Alt | Alternative HTTPS |
| 27017 | TCP | MongoDB | No auth by default in older versions |

---

## Dangerous Defaults — Check These First

> [!warning] These are the most commonly misconfigured services found in CTFs and real-world pentests

| Service | Port | Default Issue | Quick check |
|---|---|---|---|
| FTP | 21 | Anonymous login enabled | `ftp target` → user: `anonymous` |
| Telnet | 23 | Plaintext everything | `telnet target 23` |
| SNMP | 161 | Community string = `public` | `snmpwalk -c public -v2c target` |
| SMB | 445 | Null session / open shares | `smbclient -L //target -N` |
| Redis | 6379 | No auth | `redis-cli -h target` → `INFO` |
| MongoDB | 27017 | No auth | `mongo target` |
| VNC | 5900 | Weak/no password | `vncviewer target` |
| MySQL | 3306 | Root with no password | `mysql -h target -u root` |
| Tomcat | 8080 | Default admin creds `tomcat:tomcat` | `http://target:8080/manager` |

---

## What Open Ports Tell You

```
Port 22 open     → Linux box, SSH access possible
Port 80/443 open → Web server → run Gobuster/Nikto
Port 445 open    → Windows or Samba → enum4linux
Port 3306 open   → MySQL directly accessible from outside (misconfiguration!)
Port 3389 open   → Windows RDP → brute force or look for RDP CVEs
Port 21 open     → FTP → try anonymous login first
```

---

## Nmap — Quick Port Discovery Reference

```bash
nmap target                       # top 1000 ports
nmap -p- target                    # all 65535 ports (slow but thorough)
nmap -p 22,80,443 target            # specific ports
nmap -sV -p 80,443 target           # service version detection
nmap --open target                   # only show open ports (cleaner output)
```

→ Full Nmap reference in [[05_Nmap_and_Recon]]
