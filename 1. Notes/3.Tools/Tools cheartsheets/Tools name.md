---

## tags: [pentesting, recon, osint, tools]

# Recon Tools

Reference list of tools and websites for reconnaissance during pentesting/bug bounty - organized by phase.

---

## 1. Sub-Domain Enumeration

### 1.1 CLI / Installable Tools

|Tool|Description|Git Repo|
|---|---|---|
|Sublist3r|Enumerates subdomains using search engines (Google, Bing, Yahoo, etc.)|https://github.com/aboul3la/Sublist3r|
|Amass|OWASP tool for in-depth subdomain enumeration & network mapping (active + passive)|https://github.com/owasp-amass/amass|
|Subfinder|Fast passive subdomain discovery tool by ProjectDiscovery|https://github.com/projectdiscovery/subfinder|
|Assetfinder|Finds domains/subdomains related to a given domain|https://github.com/tomnomnom/assetfinder|
|findomain|Fast cross-platform subdomain enumerator|https://github.com/findomain/findomain|
|massdns|High-performance DNS resolver, often used to resolve large subdomain lists|https://github.com/blechschmidt/massdns|
|dnsx|Fast DNS toolkit for resolving/probing discovered subdomains|https://github.com/projectdiscovery/dnsx|
|httpx|Probes discovered subdomains to check which are alive (HTTP/HTTPS)|https://github.com/projectdiscovery/httpx|
|Knockpy|Python tool to enumerate subdomains via wordlists + DNS|https://github.com/guelfoweb/knock|

### 1.2 Web-Based / Passive Sources

|Website|Description|Link|
|---|---|---|
|crt.sh|Certificate Transparency log search — reveals subdomains from SSL certs|https://crt.sh/|
|Censys|Search engine for internet-connected devices/certificates|https://search.censys.io/|
|Shodan|Search engine for exposed devices, services, and subdomains|https://www.shodan.io/|
|SecurityTrails|DNS/domain history and subdomain data|https://securitytrails.com/|
|DNSdumpster|Free domain research tool showing subdomains & DNS records|https://dnsdumpster.com/|
|VirusTotal|Passive DNS data can reveal subdomains under "Relations" tab|https://www.virustotal.com/|
|Rapid7 Sonar (FDNS)|Public dataset of forward DNS records|https://opendata.rapid7.com/sonar.fdns_v2/|

---

## 2. Email Reconnaissance

### 2.1 CLI / Installable Tools

|Tool|Description|Git Repo|
|---|---|---|
|theHarvester|Gathers emails, subdomains, names, and IPs from public sources|https://github.com/laramies/theHarvester|
|Infoga|Gathers email account info (breaches, sources) from public sources|https://github.com/m4ll0k/Infoga|
|GHunt|OSINT tool to investigate Google accounts linked to an email|https://github.com/mxrch/GHunt|
|Holehe|Checks if an email is registered on various websites|https://github.com/megadose/holehe|
|Mosint|Automated email OSINT tool (breaches, socials, deliverability)|https://github.com/alpkeskin/mosint|

### 2.2 Web-Based Tools

|Website|Description|Link|
|---|---|---|
|Hunter.io|Finds and verifies professional email addresses tied to a domain|https://hunter.io/|
|Have I Been Pwned|Checks if an email/domain has appeared in known data breaches|https://haveibeenpwned.com/|
|EmailRep.io|Reputation/risk score lookup for an email address|https://emailrep.io/|
|Epieos|Reverse email lookup (Google/social account association)|https://epieos.com/|
|PhoneBook.cz|OSINT search for emails, subdomains, and URLs linked to a domain|https://phonebook.cz/|
|IntelligenceX|Search engine indexing leaks, darknet, and public data (email/domain search)|https://intelx.io/|

---

## Notes

- Combine passive sources (crt.sh, Amass passive, theHarvester) first to avoid detection, then run active resolution (dnsx, httpx, massdns) to confirm live hosts.
- Always check tool usage/legal scope before running active enumeration against a target.