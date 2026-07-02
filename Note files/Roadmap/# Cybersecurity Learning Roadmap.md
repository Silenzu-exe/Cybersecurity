# Cybersecurity Learning Roadmap

A complete guide from beginner to advanced cybersecurity professional.

---

## Overview

**Timeline:** 12-18 months (self-paced)  
**Goal:** Build practical cybersecurity skills for career or professional growth  
**Approach:** Hands-on learning with theory fundamentals

---

## Phase 1: Foundation (Months 1-3)

### 1.1 Computer Fundamentals
**What to Learn:**
- How computers work (CPU, RAM, Storage, OS)
- Binary, hexadecimal number systems
- File systems (NTFS, ext4, FAT32)
- Basic hardware components

**Resources:**
- CompTIA IT Fundamentals+ (ITF+)
- Professor Messer free videos
- Practice: Build/disassemble a computer

**Time:** 2-3 weeks

---

### 1.2 Operating Systems

#### Linux (Priority!)
[[1.1  Commands Cheat Sheet]]
**Essential Skills:**
- Command line navigation
- File permissions and ownership
- User and group management
- Process management
- Package management
- Shell scripting basics

**Practice:**
- Install Ubuntu or Kali Linux
- Complete Linux commands daily
- Set up a Linux server (home lab or VM)

**Resources:**
- Linux Journey (linuxjourney.com)
- OverTheWire Bandit wargame
- Your Linux Commands Cheat Sheet
- **Exercism** → coding practice
- **HackerRank** → problem solving
- **KodeKloud (free labs)** → Linux/DevOps hands-on

**Time:** 3-4 weeks

#### Windows
**Essential Skills:**
- Windows Server basics
- Active Directory fundamentals
- PowerShell basics
- Group Policy
- Windows security features

**Resources:**
- Microsoft Virtual Academy
- Windows Server on VirtualBox

**Time:** 2-3 weeks

---

### 1.3 Networking Fundamentals (CRITICAL!)
**What to Learn:**
[[1. Networking]]
**Core Concepts:**
- OSI Model (7 layers)
- TCP/IP Model (4 layers)
- IP addressing (IPv4, IPv6)
- Subnetting and CIDR
- MAC addresses
- DNS, DHCP
- Routing and switching basics

**Protocols to Know:**
- TCP vs UDP
- HTTP/HTTPS
- FTP/SFTP
- SSH
- SMTP, POP3, IMAP
- Telnet
- ICMP

**Tools:**
- Wireshark (packet analysis)
- nmap (network scanning)
- netcat
- ping, traceroute, netstat

**Practice Projects:**
- Set up home network
- Capture and analyze packets
- Scan your own network (legally!)
- Configure basic firewall rules

**Certifications to Consider:**
- CompTIA Network+ (highly recommended)
- Cisco CCNA (optional but valuable)

**Resources:**
- Professor Messer Network+ course (free)
- NetworkChuck YouTube channel
- Practical Networking (practicalnetworking.net)

**Time:** 4-6 weeks

---

### 1.4 Programming & Scripting (Essential!)

#### Python (Priority #1)
**Why:** Most versatile for cybersecurity

**What to Learn:**
- Basic syntax and data types
- Functions and modules
- File operations
- Working with APIs
- Regular expressions
- Libraries: requests, socket, scapy

**Practice:**
- Write port scanner
- Create password generator
- Build simple network tool
- Automate tasks

**Resources:**
- Automate the Boring Stuff with Python (free book)
- Python for Cybersecurity on YouTube
- Codecademy Python course

**Time:** 4-5 weeks

#### Bash/Shell Scripting
**What to Learn:**
- Variables and loops
- Conditionals
- Functions
- Text processing (grep, sed, awk)
- Automation scripts

**Practice:**
- Automate log analysis
- Create backup scripts
- Build system monitoring tools

**Time:** 2 weeks

#### Other Useful Languages:
- **JavaScript** - For web security
- **PowerShell** - For Windows security
- **C/C++** - Understanding exploits
- **SQL** - Database security

**Time for basics:** 1 week each

---

## Phase 2: Core Security Concepts (Months 4-6)

### 2.1 Information Security Basics

**CIA Triad:**
- **C**onfidentiality - Keeping data private
- **I**ntegrity - Ensuring data accuracy
- **A**vailability - Ensuring access when needed

**Key Concepts:**
- Authentication vs Authorization
- Encryption (symmetric vs asymmetric)
- Hashing (MD5, SHA, bcrypt)
- Digital signatures and certificates
- PKI (Public Key Infrastructure)
- SSL/TLS
- Access control models (DAC, MAC, RBAC)
- Defense in depth
- Principle of least privilege
- Zero trust architecture

**Time:** 2-3 weeks

---

### 2.2 Web Application Security

**What to Learn:**

**How Web Works:**
- HTTP methods (GET, POST, PUT, DELETE)
- Cookies and sessions
- Same-origin policy
- CORS

**Common Vulnerabilities (OWASP Top 10):**
1. **SQL Injection** - Injecting malicious SQL
2. **XSS (Cross-Site Scripting)** - Injecting malicious scripts
3. **CSRF (Cross-Site Request Forgery)** - Forcing unwanted actions
4. **Authentication flaws** - Weak login systems
5. **Security misconfiguration** - Default/poor settings
6. **Sensitive data exposure** - Unencrypted data
7. **XXE (XML External Entity)** - XML parsing attacks
8. **Broken access control** - Improper permissions
9. **Insecure deserialization** - Object injection
10. **Using components with known vulnerabilities** - Outdated libraries

**Tools:**
- Burp Suite (web proxy)
- OWASP ZAP
- SQLmap
- Browser developer tools

**Practice:**
- OWASP WebGoat
- DVWA (Damn Vulnerable Web Application)
- PortSwigger Web Security Academy (free)
- HackTheBox web challenges

**Time:** 4-5 weeks

---

### 2.3 Cryptography

**What to Learn:**

**Encryption Types:**
- **Symmetric:** AES, DES, 3DES, Blowfish
- **Asymmetric:** RSA, ECC, Diffie-Hellman
- **Hashing:** MD5, SHA-1, SHA-256, bcrypt, PBKDF2

**Concepts:**
- How encryption works
- When to use symmetric vs asymmetric
- Digital signatures
- Certificates and PKI
- SSL/TLS handshake
- Password hashing best practices
- Salt and pepper

**Tools:**
- OpenSSL
- GPG
- HashCat
- John the Ripper

**Practice:**
- Encrypt/decrypt files
- Generate SSH keys
- Create self-signed certificates
- Crack weak passwords (ethically)

**Resources:**
- Crypto101 (free book)
- Khan Academy Cryptography course

**Time:** 3-4 weeks

---

### 2.4 System & Network Security

**What to Learn:**

**Firewalls:**
- Types (packet filtering, stateful, application layer)
- iptables (Linux)
- Windows Firewall
- pfSense

**IDS/IPS:**
- Signature-based vs anomaly-based
- Snort
- Suricata

**VPN:**
- How VPNs work
- IPSec vs SSL VPN
- OpenVPN setup

**Wireless Security:**
- WEP, WPA, WPA2, WPA3
- Wireless attacks (deauth, evil twin)
- Airodump-ng, Aircrack-ng

**Email Security:**
- SPF, DKIM, DMARC
- Phishing detection
- Email headers analysis

**Practice:**
- Configure firewall rules
- Set up IDS with Snort
- Analyze network traffic
- Secure wireless network

**Time:** 4-5 weeks

---

## Phase 3: Offensive Security - Ethical Hacking (Months 7-10)

### 3.1 Penetration Testing Methodology

**Phases:**
1. **Reconnaissance** - Information gathering
2. **Scanning** - Finding vulnerabilities
3. **Gaining Access** - Exploitation
4. **Maintaining Access** - Persistence
5. **Covering Tracks** - Hiding evidence

**Time:** 1 week to understand framework

---

### 3.2 Reconnaissance & Information Gathering

**Passive Recon:**
- Google dorking
- WHOIS lookup
- DNS enumeration
- Social media OSINT
- Shodan
- theHarvester

**Active Recon:**
- Port scanning (nmap)
- Service enumeration
- Banner grabbing
- Network mapping

**Tools:**
- nmap
- Shodan
- Maltego
- Recon-ng
- theHarvester
- OSINT Framework

**Practice:**
- Gather info on target (legally!)
- Map network topology
- Identify services and versions

**Time:** 2-3 weeks

---

### 3.3 Vulnerability Scanning & Analysis

**What to Learn:**
- Types of vulnerabilities
- CVE database
- CVSS scoring
- Vulnerability scanners

**Tools:**
- Nessus
- OpenVAS
- Nikto (web scanner)
- Nuclei

**Practice:**
- Scan vulnerable VMs
- Read vulnerability reports
- Prioritize vulnerabilities

**Time:** 2 weeks

---

### 3.4 Exploitation

**What to Learn:**

**Exploit Types:**
- Buffer overflow
- Code injection
- Privilege escalation
- Remote code execution

**Exploitation Frameworks:**
- **Metasploit** (essential!)
- ExploitDB
- SearchSploit

**Common Exploits:**
- EternalBlue (SMB)
- Shellshock (Bash)
- Log4Shell (Log4j)
- SQL injection
- Command injection

**Practice Platforms:**
- **Metasploitable** (vulnerable VM)
- **VulnHub** machines
- **HackTheBox** (HTB)
- **TryHackMe** (beginner-friendly)
- **PentesterLab**

**Skills to Develop:**
- Using Metasploit
- Writing custom exploits
- Payload generation (msfvenom)
- Privilege escalation (Linux & Windows)
- Post-exploitation

**Time:** 6-8 weeks

---

### 3.5 Password Attacks

**Attack Types:**
- Brute force
- Dictionary attack
- Rainbow tables
- Password spraying
- Credential stuffing

**Tools:**
- John the Ripper
- Hashcat
- Hydra
- Medusa
- CeWL (wordlist generator)

**Practice:**
- Crack password hashes
- Test password strength
- Create custom wordlists

**Time:** 2 weeks

---

### 3.6 Social Engineering

**What to Learn:**
- Phishing (email, SMS, voice)
- Pretexting
- Baiting
- Tailgating
- Psychological manipulation

**Tools:**
- SET (Social Engineer Toolkit)
- Gophish
- Email spoofing

**Practice:**
- Create phishing scenarios (ethical!)
- Analyze phishing emails
- Build awareness programs

**Time:** 1-2 weeks

---

## Phase 4: Defensive Security - Blue Team (Months 8-11)

### 4.1 Incident Response

**IR Lifecycle:**
1. Preparation
2. Identification
3. Containment
4. Eradication
5. Recovery
6. Lessons Learned

**What to Learn:**
- IR frameworks (NIST, SANS)
- Forensics basics
- Log analysis
- Threat hunting
- Malware analysis basics

**Tools:**
- SIEM (Splunk, ELK Stack)
- Volatility (memory forensics)
- Autopsy (disk forensics)
- Wireshark

**Time:** 3-4 weeks

---

### 4.2 Security Monitoring & SIEM

**What to Learn:**
- Log collection and analysis
- Correlation rules
- Alerting and dashboards
- Threat intelligence integration

**Tools:**
- **Splunk** (most popular)
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Graylog
- Security Onion

**Practice:**
- Set up SIEM
- Create detection rules
- Analyze logs for threats
- Build dashboards

**Resources:**
- Splunk Fundamentals (free course)
- Boss of the SOC datasets

**Time:** 3-4 weeks

---

### 4.3 Malware Analysis

**Types:**
- **Static Analysis** - Without executing
- **Dynamic Analysis** - Running in sandbox
- **Behavioral Analysis** - Monitoring actions

**Tools:**
- IDA Pro / Ghidra (reverse engineering)
- OllyDbg
- ANY.RUN (online sandbox)
- VirusTotal
- REMnux (malware analysis Linux)

**Practice:**
- Analyze malware samples (in isolated VM!)
- Understand common malware behaviors
- Write YARA rules

**Time:** 3-4 weeks

---

### 4.4 Threat Intelligence

**What to Learn:**
- IOCs (Indicators of Compromise)
- TTPs (Tactics, Techniques, Procedures)
- MITRE ATT&CK framework
- Threat actor profiling
- Cyber kill chain

**Sources:**
- OSINT feeds
- VirusTotal Intelligence
- AlienVault OTX
- MISP

**Time:** 2 weeks

---

## Phase 5: Specialization (Months 12+)

Choose one or more paths to specialize:

### 5.1 Cloud Security
**Focus:**
- AWS/Azure/GCP security
- Container security (Docker, Kubernetes)
- Serverless security
- IAM (Identity and Access Management)
- Cloud compliance

**Certifications:**
- AWS Certified Security - Specialty
- Azure Security Engineer Associate
- CCSP (Certified Cloud Security Professional)

---

### 5.2 Mobile Security
**Focus:**
- Android security
- iOS security
- Mobile app testing (OWASP Mobile Top 10)
- Reverse engineering mobile apps

**Tools:**
- Frida
- MobSF
- Apktool
- Burp Suite Mobile Assistant

---

### 5.3 IoT Security
**Focus:**
- Embedded systems
- Firmware analysis
- Hardware hacking
- Wireless protocols (Bluetooth, Zigbee)

**Tools:**
- Binwalk
- Firmware analysis toolkit
- Logic analyzers
- Software-defined radio

---

### 5.4 Application Security (AppSec)
**Focus:**
- Secure coding practices
- Code review
- SAST/DAST tools
- DevSecOps
- Security in SDLC

**Tools:**
- SonarQube
- Checkmarx
- Veracode
- OWASP Dependency-Check

---

### 5.5 Red Team / Adversary Simulation
**Focus:**
- Advanced persistent threats (APT)
- Evasion techniques
- Custom tool development
- Command and control (C2)
- Living off the land

**Tools:**
- Cobalt Strike
- Empire
- Covenant
- BloodHound (Active Directory)

---

### 5.6 Governance, Risk & Compliance (GRC)
**Focus:**
- Security frameworks (NIST, ISO 27001, CIS)
- Risk assessment
- Compliance auditing
- Security policies
- Business continuity

**Certifications:**
- CRISC
- CISM
- ISO 27001 Lead Auditor

---

## Certifications Roadmap

### Entry Level
1. **CompTIA Security+** (Start here!)
   - Covers security fundamentals
   - Widely recognized
   - Time: 2-3 months prep

2. **CompTIA Network+**
   - Essential networking knowledge
   - Good foundation for security

### Intermediate
3. **CEH (Certified Ethical Hacker)**
   - Offensive security focus
   - Good for penetration testing career

4. **CompTIA CySA+** (Cybersecurity Analyst)
   - Defensive security focus
   - SOC analyst preparation

5. **GIAC GSEC** (Security Essentials)
   - SANS training (expensive but excellent)

### Advanced - Offensive
6. **OSCP** (Offensive Security Certified Professional)
   - HIGHLY respected
   - 24-hour practical exam
   - Proves hands-on skills
   - "Try Harder" mentality

7. **OSWE** (Offensive Security Web Expert)
   - Advanced web exploitation

8. **OSCE** (Offensive Security Certified Expert)
   - Expert-level exploitation

### Advanced - Defensive
9. **GCIH** (GIAC Certified Incident Handler)
   - Incident response

10. **GCFA** (GIAC Certified Forensic Analyst)
    - Digital forensics

### Expert Level
11. **CISSP** (Certified Information Systems Security Professional)
    - Requires 5 years experience
    - Management/architect level
    - Expensive but prestigious

12. **CISM** (Certified Information Security Manager)
    - Management focus

---

## Hands-On Practice Platforms

### Beginner-Friendly
- **TryHackMe** - Guided learning paths
- **PicoCTF** - CTF for beginners
- **OverTheWire** - Wargames

### Intermediate
- **HackTheBox** - Active machines (harder)
- **VulnHub** - Downloadable vulnerable VMs
- **PentesterLab** - Web security focus

### Advanced
- **HackTheBox Pro Labs** - Enterprise environments
- **Offensive Security Proving Grounds** - OSCP prep
- **SANS NetWars** - Competitive CTF

### CTF Competitions
- **CTFtime.org** - Find competitions
- **PicoCTF** - Annual competition
- **Google CTF**
- **DEF CON CTF**

---

## Building Your Home Lab

### Essential Components

**Hardware Option:**
- Old laptop/desktop
- 16GB+ RAM recommended
- Install hypervisor (VirtualBox, VMware)

**Cloud Option (Free Tiers):**
- AWS Free Tier
- Azure Free Tier
- Google Cloud Free Tier

### VMs to Set Up
1. **Kali Linux** - Penetration testing tools
2. **Metasploitable** - Vulnerable target
3. **Windows Server** - Active Directory practice
4. **Ubuntu Server** - Linux hardening
5. **Security Onion** - SIEM/IDS
6. **pfSense** - Firewall practice

### Lab Projects
- Set up Active Directory domain
- Configure SIEM and generate logs
- Simulate attacks and detect them
- Practice incident response
- Build vulnerable web app and secure it

---

## Daily Habits for Success

### 1. Read Security News (15-30 min/day)
**Sources:**
- **Krebs on Security**
- **The Hacker News**
- **Bleeping Computer**
- **Dark Reading**
- **/r/netsec** subreddit
- **Twitter:** Follow security researchers

### 2. Practice Hands-On (1-2 hours/day)
- Complete CTF challenges
- Work on home lab
- Code security tools
- Practice on HackTheBox/TryHackMe

### 3. Watch Security Content
**YouTube Channels:**
- **NetworkChuck**
- **John Hammond**
- **IppSec** (HackTheBox walkthroughs)
- **LiveOverflow**
- **The Cyber Mentor**
- **David Bombal**

**Podcasts:**
- Darknet Diaries
- Risky Business
- Security Now

### 4. Participate in Community
- Join security Discord servers
- Attend local meetups (BSides, OWASP)
- Contribute to open-source security tools
- Write blog posts about what you learn

---

## Career Paths in Cybersecurity

### Entry-Level Roles
1. **SOC Analyst (Tier 1)**
   - Monitor security alerts
   - Initial triage
   - Salary: $50-70k

2. **IT Security Specialist**
   - General security tasks
   - Policy implementation
   - Salary: $55-75k

3. **Junior Penetration Tester**
   - Vulnerability scanning
   - Basic testing
   - Salary: $60-80k

### Mid-Level Roles
4. **Security Engineer**
   - Implement security solutions
   - Hardening systems
   - Salary: $80-120k

5. **Penetration Tester**
   - Full penetration testing
   - Report writing
   - Salary: $85-130k

6. **Security Analyst**
   - Threat analysis
   - Incident response
   - Salary: $75-110k

7. **Forensics Analyst**
   - Digital forensics
   - Evidence collection
   - Salary: $80-120k

### Senior-Level Roles
8. **Security Architect**
   - Design security systems
   - Enterprise security
   - Salary: $120-180k

9. **Red Team Lead**
   - Advanced offensive operations
   - Team management
   - Salary: $130-200k+

10. **CISO (Chief Information Security Officer)**
    - Executive leadership
    - Strategy and governance
    - Salary: $150-300k+

---

## Common Mistakes to Avoid

### 1. Certificate Hunting Without Skills
❌ **Don't:** Just collect certifications without practicing
✅ **Do:** Build practical skills, then get certified

### 2. Only Learning Theory
❌ **Don't:** Just watch videos and read books
✅ **Do:** 70% hands-on practice, 30% theory

### 3. Skipping Fundamentals
❌ **Don't:** Jump straight to hacking tools
✅ **Do:** Master networking, OS, programming first

### 4. Isolating Yourself
❌ **Don't:** Learn alone without community
✅ **Do:** Join Discord, attend meetups, ask questions

### 5. Not Documenting Your Learning
❌ **Don't:** Forget what you learned
✅ **Do:** Take notes, write blog posts, create cheat sheets

### 6. Illegal Activities
❌ **Don't:** Hack systems without permission
✅ **Do:** Use legal practice platforms and get written authorization

### 7. Tutorial Hell
❌ **Don't:** Endlessly follow tutorials
✅ **Do:** Build your own projects after basics

---

## Your 30-Day Quick Start Plan

### Week 1: Linux & Networking
- **Days 1-3:** Install Kali Linux, learn basic commands
- **Days 4-7:** Study OSI model, TCP/IP, practice with Wireshark

### Week 2: Programming & Web
- **Days 8-10:** Python basics, write simple scripts
- **Days 11-14:** Learn how web works, HTTP, cookies

### Week 3: Security Basics
- **Days 15-17:** CIA triad, encryption basics, OWASP Top 10
- **Days 18-21:** Set up home lab, install vulnerable VMs

### Week 4: Hands-On Practice
- **Days 22-24:** Complete TryHackMe beginner rooms
- **Days 25-27:** Try first CTF challenge
- **Days 28-30:** Set up GitHub, document learning, plan next steps

---

## Resources Summary

### Free Learning Platforms
- **TryHackMe** - Guided cybersecurity training
- **HackTheBox Academy** - Free courses available
- **Cybrary** - Free and paid courses
- **Professor Messer** - Free certification training
- **YouTube** - Endless free content

### Books (Highly Recommended)
1. **"The Web Application Hacker's Handbook"** - Web security bible
2. **"Metasploit: The Penetration Tester's Guide"** - Exploitation
3. **"Black Hat Python"** - Python for hackers
4. **"The Hacker Playbook 3"** - Practical penetration testing
5. **"RTFM: Red Team Field Manual"** - Quick reference

### Paid Platforms (Worth It)
- **Offensive Security** (OSCP training)
- **SANS** courses (expensive but best quality)
- **INE** (Pentesting and networking)
- **Pluralsight** - Tech courses

### Communities to Join
- **Reddit:** r/netsec, r/AskNetsec, r/cybersecurity
- **Discord:** TryHackMe, HackTheBox, Cybersecurity servers
- **Twitter:** Security researchers and professionals
- **LinkedIn:** Connect with professionals

---

## Final Tips

### Mindset for Success
1. **Be patient** - This takes time (12-18+ months)
2. **Stay curious** - Always ask "how does this work?"
3. **Practice daily** - Consistency beats intensity
4. **Learn from failures** - Every failed CTF is a lesson
5. **Give back** - Help beginners when you can
6. **Stay ethical** - Only hack with permission
7. **Keep learning** - Cybersecurity constantly evolves

### Your First Job
- Start applying after 6-9 months of learning
- Build a portfolio (GitHub, blog, CTF write-ups)
- Network at meetups and conferences
- Consider internships
- Entry-level SOC analyst is common first role
- Certifications help but skills matter more

### Remember
**"The expert in anything was once a beginner."**

Cybersecurity is challenging but incredibly rewarding. Stay persistent, keep learning, and you'll get there!

---

## Quick Reference: Your Next Steps

**Right Now:**
1. Install Kali Linux (VM or dual boot)
2. Start TryHackMe "Complete Beginner" path
3. Join cybersecurity Discord/Reddit
4. Set a daily learning goal (1-2 hours minimum)

**This Month:**
1. Complete Linux basics
2. Learn Python fundamentals
3. Understand networking (OSI, TCP/IP)
4. Finish 10 TryHackMe rooms

**This Quarter:**
1. Start studying for Security+ certification
2. Complete OWASP Top 10 vulnerabilities
3. Build home lab with 3+ VMs
4. Root your first HackTheBox machine

**This Year:**
1. Get Security+ certified
2. Complete 50+ CTF challenges
3. Build portfolio with projects and write-ups
4. Apply for entry-level security roles

---

*This roadmap is a guide, not a rigid path. Adjust based on your goals, pace, and interests. Good luck on your cybersecurity journey! 🔒*


---

| Resource         | Type                    | Cost      |
| ---------------- | ----------------------- | --------- |
| TryHackMe        | Learning Platform       | Free tier |
| Hack The Box     | CTF/Labs                | Free tier |
| PortSwigger      | Web Security            | 100% Free |
| OverTheWire      | Linux/Security Wargames | 100% Free |
| picoCTF          | CTF for Beginners       | 100% Free |
| Professor Messer | Video Courses           | 100% Free |
| LetsDefend       | Blue Team Training      | Free tier |
| CyberSecLabs     | Practice Labs           | Free tier |
