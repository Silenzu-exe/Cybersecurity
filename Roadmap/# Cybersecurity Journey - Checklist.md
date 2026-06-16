# Cybersecurity Journey - Progress Checklist

Track your progress through your cybersecurity learning journey. Check off items as you complete them!

**Started:** [2082-10-11]  
**Target Completion:** [2085-10-01] _(revised: ~24 months at 3-5 hrs/week, was 15 months)_

> **Note on pacing:** Original plan assumed higher weekly hours. At 3-5 hrs/week alongside BSc CSIT coursework, this is realistically a 22-24 month journey — and that's fine. Use semester breaks (Dashain, winter, post-board-exams) for intensive 10-15 hr/week pushes on HackTheBox/CTFs to catch up.

> **Note on certifications:** Security+, Network+, CEH, OSCP, CISSP exams all cost money. Study materials (Professor Messer, PWK videos, etc.) are free. Treat cert checkboxes below as "study the material" — only pursue the actual exam if you find student discounts/vouchers later.

> **Python project ideas (from earlier 24-week plan, slot these into the relevant Python sections below):**
> 
> - Port scanner (socket module) → Month 2
> - Log file parser (top IPs by request count) → Month 4
> - Security header checker (requests library) → Month 5
> - Hash brute-forcer / wordlist cracker (ties into Cryptography coursework) → Month 6-7
> - Real-time SSH failed-login monitor → Months 15-17 (Blue Team/SIEM phase)

---

[[Cyber Security/# Cybersecurity Learning Roadmap]]

## 🎯 Phase 1: Foundation (Months 1-2, was 1-3 — accelerated)

### Computer Fundamentals

- [x] Understand how computers work (CPU, RAM, Storage)
- [x] Learn binary and hexadecimal number systems
- [ ] Understand file systems (NTFS, ext4, FAT32, btrfs) — _you already know ext4/btrfs from Arch_
- [x] Learn basic hardware components
- [ ] Complete CompTIA ITF+ material or equivalent _(optional — skip if pressed for time)_

**Phase 1.1 Completed:** _**/**_/___

---

### Linux Operating System (PRIORITY!) — _Mostly done via Arch daily-driving_

[[1.Linux Commands Cheat Sheet]]

- [x] Install Ubuntu or Kali Linux (VM or dual boot) — _Arch is more advanced, counts as done_
- [x] Master basic commands (ls, cd, pwd, mkdir, rm, cp, mv)
- [x] Understand file permissions (chmod, chown)
- [x] Learn user and group management
- [ ] Practice process management (ps, top, kill) — _covered in OSI/cybersecurity notes session_
- [x] Learn package management (apt, yum, dnf) — _pacman/yay daily use transfers directly_
- [ ] Write 5 basic bash scripts — _start with the log-scanning script idea_
- [ ] Complete OverTheWire Bandit levels 1-10
- [ ] Complete OverTheWire Bandit levels 11-20
- [ ] Complete OverTheWire Bandit levels 21-25
- [x] Set up a Linux server (home lab or VM) — _Arch + systemd services (Ollama, etc.) counts_

**Linux Skills Completed:** _**/**_/___

---

### Windows Operating System — _Deprioritized: moved to Months 8-10 (was Phase 1)_

> Reasoning: You're Linux/Arch-focused. AD/Windows matters more for corporate red team work later, not foundational learning. No need to block early progress on this.

- [ ] Install Windows Server (VM)
- [ ] Learn Active Directory basics
- [ ] Practice PowerShell basics (cmdlets, variables, loops)
- [ ] Understand Group Policy
- [ ] Learn Windows security features
- [ ] Create 3 PowerShell automation scripts

**Windows Skills Completed:** _**/**_/___ _(target: Months 8-10)_

---

### Networking Fundamentals (CRITICAL!) — _Theory partly covered already_

#### Core Concepts

- [ ] Memorize OSI Model (7 layers) — _covered in detail incl. security threats per layer_
- [ ] Understand TCP/IP Model (4 layers) — _covered incl. 3-way handshake & SYN flood_
- [ ] Master IPv4 addressing
- [ ] Practice subnetting (10 exercises)
- [ ] Understand CIDR notation
- [ ] Learn IPv6 basics — _covered (IPv4 vs IPv6 comparison)_
- [ ] Understand MAC addresses — _covered (OUI, spoofing, ARP poisoning)_
- [ ] Know how DNS works — _covered (resolution flow, spoofing, tunneling, DNSSEC)_
- [ ] Know how DHCP works
- [ ] Understand routing basics
- [ ] Understand switching basics

#### Protocols

- [ ] Understand TCP vs UDP
- [ ] Know HTTP/HTTPS
- [ ] Know FTP/SFTP
- [ ] Know SSH
- [ ] Know SMTP, POP3, IMAP
- [ ] Know Telnet
- [ ] Know ICMP

#### Tools & Practice

- [ ] Install and use Wireshark
- [ ] Capture and analyze 5 different packet types
- [ ] Learn nmap basics
- [ ] Scan your own network with nmap
- [ ] Use netcat for network testing
- [ ] Practice with ping, traceroute, netstat
- [ ] Set up home network with proper segmentation
- [ ] Configure basic firewall rules

#### Certification

- [ ] Study for CompTIA Network+ _(material via Professor Messer — free)_
- [ ] Pass CompTIA Network+ exam _(optional — costs money, skip unless discount found)_

**Networking Skills Completed:** _**/**_/___

---

### Programming & Scripting

#### Python (PRIORITY!)

- [x] Learn Python basics (syntax, variables, data types)
- [ ] Understand functions and modules
- [ ] Practice file operations
- [ ] Learn to work with APIs
- [ ] Master regular expressions
- [ ] Learn requests library
- [ ] Learn socket library
- [ ] Learn scapy library
- [ ] Write a port scanner
- [ ] Write a password generator
- [ ] Write a network tool (ping sweep, banner grabber, etc.)
- [ ] Complete 10 Python automation tasks
- [ ] Complete "Automate the Boring Stuff" exercises

**Python Skills Completed:** _**/**_/___

#### Bash Scripting

- [ ] Learn variables and loops
- [ ] Learn conditionals (if/else)
- [ ] Learn functions
- [ ] Master text processing (grep, sed, awk)
- [ ] Write log analysis script
- [ ] Write backup automation script
- [ ] Write system monitoring script
- [ ] Create 5 useful automation scripts

**Bash Skills Completed:** _**/**_/___

#### Other Languages (Optional)

- [ ] SQL basics (1 week) — _prioritize this one: directly useful for SQLi labs AND your PhishGuard project_
- [ ] JavaScript basics (1 week) — _useful for XSS labs; you already cover JS in Web Tech course_
- [ ] PowerShell basics (1 week) — _push to Month 8-10 with Windows section_
- [ ] C basics (1 week) — _push to later (useful for binary exploitation in Phase 3+)_

**Phase 1 COMPLETED:** _**/**_/___ _(target: Month 2-3, was Month 3)_

---

## 🔒 Phase 2: Core Security Concepts (Months 3-7, was 4-6 — extended for realistic pacing)

### Information Security Basics

- [x] Understand CIA Triad (Confidentiality, Integrity, Availability) — _covered in Cryptography coursework_
- [ ] Know Authentication vs Authorization
- [ ] Understand encryption (symmetric vs asymmetric) — _sync with Cryptography course schedule_
- [ ] Understand hashing (MD5, SHA, bcrypt)
- [ ] Know digital signatures — _covered in Cryptography coursework_
- [ ] Understand PKI (Public Key Infrastructure)
- [ ] Understand SSL/TLS
- [ ] Know access control models (DAC, MAC, RBAC)
- [ ] Understand defense in depth
- [ ] Know principle of least privilege
- [ ] Understand zero trust architecture

**InfoSec Basics Completed:** _**/**_/___

---

### Web Application Security

#### Foundation

- [ ] Understand HTTP methods (GET, POST, PUT, DELETE)
- [ ] Know how cookies and sessions work
- [ ] Understand same-origin policy
- [ ] Understand CORS

#### OWASP Top 10 (2021)

- [ ] SQL Injection - Understand and exploit _(start here — links to your "weeks 9-10" plan)_
- [ ] XSS (Cross-Site Scripting) - Understand and exploit
- [ ] CSRF (Cross-Site Request Forgery) - Understand and exploit
- [ ] Authentication flaws - Identify and exploit
- [ ] Security misconfiguration - Identify
- [ ] Sensitive data exposure - Identify
- [ ] XXE (XML External Entity) - Understand
- [ ] Broken access control - Identify and exploit
- [ ] Insecure deserialization - Understand
- [ ] Using components with known vulnerabilities - Identify

#### Tools

- [ ] Install and configure Burp Suite
- [ ] Complete 5 challenges with Burp Suite
- [ ] Install OWASP ZAP
- [ ] Use SQLmap on vulnerable target
- [ ] Master browser developer tools

#### Practice

- [ ] Complete OWASP WebGoat exercises
- [ ] Complete DVWA (Damn Vulnerable Web App) challenges
- [ ] Complete PortSwigger Academy SQL Injection labs
- [ ] Complete PortSwigger Academy XSS labs
- [ ] Complete PortSwigger Academy CSRF labs
- [ ] Solve 10 HackTheBox web challenges

**Web Security Completed:** _**/**_/___

---

### Cryptography — _Major overlap with your BSc CSIT Cryptography course_

#### Concepts

- [ ] Understand symmetric encryption (AES, DES, 3DES) — _covered in coursework_
- [ ] Understand asymmetric encryption (RSA, ECC) — _RSA already studied for board exams_
- [ ] Understand Diffie-Hellman key exchange — _covered in coursework_
- [ ] Know hashing algorithms (MD5, SHA-1, SHA-256, bcrypt)
- [ ] Understand digital signatures — _covered in coursework_
- [ ] Understand SSL/TLS handshake process
- [ ] Know password hashing best practices
- [ ] Understand salt and pepper in hashing

#### Tools & Practice

- [ ] Use OpenSSL to encrypt/decrypt files
- [ ] Generate and use GPG keys
- [ ] Create self-signed SSL certificate
- [ ] Use HashCat to crack passwords (ethically)
- [ ] Use John the Ripper
- [ ] Crack 10 weak password hashes — _natural extension of your Week 8 Python hash-cracker project_

#### Learning

- [ ] Read Crypto101 book or complete Khan Academy course _(may overlap heavily with coursework — skim, don't duplicate)_

**Cryptography Completed:** _**/**_/___ _(target: tie to your coursework exam schedule)_

---

### System & Network Security

#### Firewalls

- [ ] Understand firewall types
- [ ] Configure iptables rules (Linux)
- [ ] Configure Windows Firewall
- [ ] Set up pfSense firewall

#### IDS/IPS

- [ ] Understand signature-based vs anomaly-based detection
- [ ] Install and configure Snort
- [ ] Write 5 custom Snort rules
- [ ] Install Suricata

#### VPN

- [ ] Understand how VPNs work
- [ ] Know IPSec vs SSL VPN
- [ ] Set up OpenVPN server
- [ ] Configure VPN client

#### Wireless Security

- [ ] Understand WEP, WPA, WPA2, WPA3
- [ ] Know common wireless attacks
- [ ] Use Airodump-ng to capture packets
- [ ] Practice with Aircrack-ng (on own network!)

#### Email Security

- [ ] Understand SPF, DKIM, DMARC
- [ ] Analyze email headers
- [ ] Identify phishing emails (practice on 10 samples)

**System Security Completed:** _**/**_/___

#### Certification

- [ ] Study for CompTIA Security+ _(Professor Messer videos — free)_
- [ ] Pass CompTIA Security+ exam _(optional — check for student vouchers)_

**Phase 2 COMPLETED:** _**/**_/___ _(target: Month 7, was Month 6)_

---

## ⚔️ Phase 3: Offensive Security (Months 8-14, was 7-10 — extended)

### Penetration Testing Methodology

- [ ] Memorize penetration testing phases
- [ ] Understand each phase in detail
- [ ] Create penetration testing checklist/methodology

---

### Reconnaissance & Information Gathering

#### Passive Recon

- [ ] Master Google dorking (10 advanced dorks)
- [ ] Perform WHOIS lookups
- [ ] Enumerate DNS records
- [ ] Practice social media OSINT
- [ ] Use Shodan to find devices
- [ ] Use theHarvester to gather emails

#### Active Recon

- [ ] Master nmap (all scan types)
- [ ] Perform service enumeration
- [ ] Practice banner grabbing
- [ ] Map network topology

#### Tools Mastery

- [ ] Complete 10 OSINT investigations
- [ ] Use Maltego for reconnaissance
- [ ] Use Recon-ng
- [ ] Master OSINT Framework

**Recon Skills Completed:** _**/**_/___

---

### Vulnerability Scanning

#### Concepts

- [ ] Understand vulnerability types
- [ ] Know CVE database
- [ ] Understand CVSS scoring

#### Tools

- [ ] Install and use Nessus
- [ ] Install and use OpenVAS
- [ ] Use Nikto web scanner
- [ ] Use Nuclei

#### Practice

- [ ] Scan 5 vulnerable VMs
- [ ] Read and analyze 10 vulnerability reports
- [ ] Learn to prioritize vulnerabilities

**Vuln Scanning Completed:** _**/**_/___

---

### Exploitation

#### Foundation

- [ ] Understand buffer overflow basics
- [ ] Understand code injection
- [ ] Understand privilege escalation
- [ ] Understand remote code execution

#### Metasploit Framework

- [ ] Learn Metasploit architecture
- [ ] Use msfconsole
- [ ] Generate payloads with msfvenom
- [ ] Complete 10 exploits with Metasploit
- [ ] Practice post-exploitation techniques

#### Common Exploits

- [ ] Exploit EternalBlue (SMB)
- [ ] Exploit Shellshock (Bash)
- [ ] Practice SQL injection manually
- [ ] Practice command injection

#### Privilege Escalation

- [ ] Linux privilege escalation (5 methods)
- [ ] Windows privilege escalation (5 methods)
- [ ] Use LinPEAS and WinPEAS
- [ ] Exploit SUID binaries
- [ ] Exploit sudo misconfigurations

#### Practice Platforms

- [ ] Root Metasploitable VM
- [ ] Complete 5 VulnHub machines
- [ ] Root 10 HackTheBox easy machines
- [ ] Root 5 HackTheBox medium machines
- [ ] Complete TryHackMe Jr Penetration Tester path
- [ ] Complete 20 TryHackMe rooms
- [ ] Solve 5 PentesterLab exercises

**Exploitation Skills Completed:** _**/**_/___

---

### Password Attacks

#### Techniques

- [ ] Understand brute force attacks
- [ ] Understand dictionary attacks
- [ ] Understand rainbow tables
- [ ] Understand password spraying
- [ ] Understand credential stuffing

#### Tools

- [ ] Master John the Ripper
- [ ] Master Hashcat
- [ ] Use Hydra for password attacks
- [ ] Use Medusa
- [ ] Create custom wordlists with CeWL

#### Practice

- [ ] Crack 20 password hashes (various types)
- [ ] Create wordlist from website
- [ ] Test password strength of 10 accounts

**Password Attack Skills Completed:** _**/**_/___

---

### Social Engineering

#### Concepts

- [ ] Understand phishing (email, SMS, voice)
- [ ] Understand pretexting
- [ ] Understand baiting
- [ ] Know psychological manipulation techniques

#### Tools

- [ ] Use SET (Social Engineer Toolkit)
- [ ] Set up Gophish phishing simulation
- [ ] Practice email spoofing (ethically)

#### Practice

- [ ] Create 3 phishing scenarios (ethical training)
- [ ] Analyze 10 real phishing emails
- [ ] Develop security awareness training

**Social Engineering Completed:** _**/**_/___

**Phase 3 COMPLETED:** _**/**_/___

---

## 🛡️ Phase 4: Defensive Security (Months 8-11)

### Incident Response

#### Framework

- [ ] Memorize IR lifecycle (6 phases)
- [ ] Understand NIST IR framework
- [ ] Understand SANS IR framework

#### Skills

- [ ] Perform log analysis (5 scenarios)
- [ ] Practice threat hunting
- [ ] Understand malware analysis basics
- [ ] Create incident response plan
- [ ] Conduct tabletop exercise

#### Tools

- [ ] Learn Volatility (memory forensics)
- [ ] Learn Autopsy (disk forensics)
- [ ] Analyze 5 forensic images
- [ ] Investigate 3 simulated incidents

**Incident Response Completed:** _**/**_/___

---

### Security Monitoring & SIEM

#### Concepts

- [ ] Understand log collection
- [ ] Understand correlation rules
- [ ] Know how to create alerts
- [ ] Understand threat intelligence integration

#### Tools

- [ ] Set up Splunk (free version)
- [ ] Complete Splunk Fundamentals 1
- [ ] Complete Splunk Fundamentals 2
- [ ] Set up ELK Stack
- [ ] Set up Security Onion

#### Practice

- [ ] Ingest logs from 5 different sources
- [ ] Create 10 detection rules
- [ ] Build 3 security dashboards
- [ ] Analyze Boss of the SOC dataset
- [ ] Detect 10 different attack types in logs

**SIEM Skills Completed:** _**/**_/___

---

### Malware Analysis

#### Static Analysis

- [ ] Analyze PE file structure
- [ ] Extract strings from malware
- [ ] Analyze 5 malware samples (static)

#### Dynamic Analysis

- [ ] Set up malware analysis sandbox
- [ ] Analyze 5 malware samples (dynamic)
- [ ] Monitor registry changes
- [ ] Monitor network traffic
- [ ] Monitor file system changes

#### Tools

- [ ] Learn to use IDA Free or Ghidra
- [ ] Use ANY.RUN sandbox
- [ ] Use VirusTotal for analysis
- [ ] Install REMnux

#### Advanced

- [ ] Write 3 YARA rules
- [ ] Reverse engineer simple malware

**Malware Analysis Completed:** _**/**_/___

---

### Threat Intelligence

#### Concepts

- [ ] Understand IOCs (Indicators of Compromise)
- [ ] Understand TTPs (Tactics, Techniques, Procedures)
- [ ] Learn MITRE ATT&CK framework
- [ ] Know cyber kill chain

#### Practice

- [ ] Map 5 attacks to MITRE ATT&CK
- [ ] Create threat intelligence report
- [ ] Use VirusTotal Intelligence
- [ ] Use AlienVault OTX
- [ ] Set up MISP

**Threat Intelligence Completed:** _**/**_/___

**Phase 4 COMPLETED:** _**/**_/___

---

## 🎓 Certifications Checklist

> **Reminder:** "Studied" = used free materials. "Passed" = paid exam, optional — only pursue if you find student discounts or it becomes a job requirement later.

### Entry Level

- [ ] CompTIA Security+ - Studied
- [ ] CompTIA Security+ - Passed ✓ (Date: _______) _(optional/paid)_
- [ ] CompTIA Network+ - Studied
- [ ] CompTIA Network+ - Passed ✓ (Date: _______) _(optional/paid)_

### Intermediate

- [ ] CEH - Studied
- [ ] CEH - Passed ✓ (Date: _______) _(optional/paid)_
- [ ] CompTIA CySA+ - Studied
- [ ] CompTIA CySA+ - Passed ✓ (Date: _______) _(optional/paid)_

### Advanced

- [ ] OSCP - Started PWK course _(paid — consider only after building strong HTB portfolio)_
- [ ] OSCP - Completed 30 lab machines
- [ ] OSCP - Completed 50 lab machines
- [ ] OSCP - Passed exam ✓ (Date: _______)
- [ ] OSWE - Passed ✓ (Date: _______)

### Expert

- [ ] CISSP - Studied
- [ ] CISSP - Passed ✓ (Date: _______) _(requires 5 yrs experience — long-term goal)_

---

## 🏆 Hands-On Practice Milestones

### TryHackMe

- [ ] Complete 10 rooms
- [ ] Complete 25 rooms
- [ ] Complete 50 rooms
- [ ] Complete 100 rooms
- [ ] Complete Jr Penetration Tester path
- [ ] Complete Offensive Pentesting path
- [ ] Complete Cyber Defense path

### HackTheBox

- [ ] Root first easy machine
- [ ] Root 10 easy machines
- [ ] Root first medium machine
- [ ] Root 10 medium machines
- [ ] Root first hard machine
- [ ] Root 5 hard machines
- [ ] Solve first challenge
- [ ] Solve 20 challenges
- [ ] Achieve Hacker rank
- [ ] Achieve Pro Hacker rank

### VulnHub

- [ ] Root 5 beginner VMs
- [ ] Root 5 intermediate VMs
- [ ] Root 5 advanced VMs

### CTF Competitions

- [ ] Participate in first CTF
- [ ] Participate in 5 CTFs
- [ ] Win first flag in competition
- [ ] Place in top 50% of a CTF
- [ ] Place in top 25% of a CTF

---

## 🏠 Home Lab Progress

### Infrastructure

- [ ] Set up hypervisor (VirtualBox/VMware)
- [ ] Create network diagram for lab
- [ ] Configure isolated virtual network

### Virtual Machines

- [ ] Kali Linux installed and configured
- [ ] Metasploitable installed
- [ ] Windows Server with Active Directory
- [ ] Ubuntu Server installed
- [ ] Security Onion installed
- [ ] pfSense firewall configured

### Projects

- [ ] Set up Active Directory domain
- [ ] Configure SIEM to collect logs
- [ ] Simulate and detect attack
- [ ] Practice incident response scenario
- [ ] Build vulnerable web app
- [ ] Secure vulnerable web app
- [ ] Set up honeypot

---

## 📚 Learning Resources Completed

### Books Read

- [ ] The Web Application Hacker's Handbook
- [ ] Metasploit: The Penetration Tester's Guide
- [ ] Black Hat Python
- [ ] The Hacker Playbook 3
- [ ] RTFM: Red Team Field Manual
- [ ] Automate the Boring Stuff with Python

### Courses Completed

- [ ] Professor Messer Security+
- [ ] Professor Messer Network+
- [ ] TryHackMe Complete Beginner path
- [ ] TryHackMe Jr Penetration Tester path
- [ ] PortSwigger Web Security Academy
- [ ] Splunk Fundamentals

---

## 🌟 Career Development

### Portfolio

- [ ] Create GitHub account
- [ ] Upload 5 security tools/scripts
- [ ] Upload 10 security tools/scripts
- [ ] Start security blog
- [ ] Write 5 blog posts (CTF write-ups, tutorials, etc.)
- [ ] Write 10 blog posts
- [ ] Create LinkedIn profile
- [ ] Document home lab setup

### Networking

- [ ] Join cybersecurity Discord server
- [ ] Join r/netsec and r/AskNetsec
- [ ] Attend first local security meetup
- [ ] Attend BSides conference
- [ ] Connect with 10 security professionals on LinkedIn
- [ ] Connect with 25 security professionals on LinkedIn

### Job Hunting

- [ ] Update resume with security skills
- [ ] Apply to first security job
- [ ] Apply to 10 security jobs
- [ ] Get first interview
- [ ] Receive job offer ✓ (Congratulations!)

---


---

