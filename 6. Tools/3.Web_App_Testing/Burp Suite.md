---
tags: [pentesting, web-security, tools, burpsuite, cheatsheet]
---

# Burp Suite

---

## What Is Burp Suite?

Burp Suite is an **integrated platform for testing the security of web applications**, made by PortSwigger. It's the industry-standard tool for web app pentesting and bug bounty hunting.

At its core, Burp works as an **intercepting proxy** — it sits between your browser and the target website, letting you see, pause, and modify every single request and response that passes through, instead of just watching traffic like Wireshark does.

**Editions:**
| Edition | What you get |
|---|---|
| **Community (Free)** | Proxy, Repeater, Intruder (heavily rate-limited), Decoder, Comparer, Sequencer — enough to learn and do manual testing |
| **Professional (Paid)** | Full-speed Intruder, the automated Scanner, saving/restoring projects, extensions via BApp Store |
| **Enterprise** | CI/CD-integrated automated scanning for orgs |

---

## What It Does

Burp Suite lets you:
- **See every HTTP/HTTPS request and response** your browser makes to a site — headers, cookies, parameters, body — nothing hidden.
- **Intercept and edit requests before they're sent** — change a parameter, a cookie, a hidden field, then forward it.
- **Replay and tweak requests repeatedly** to test how the server reacts to different input (core of manual testing).
- **Automate sending thousands of payload variations** to a single request to fuzz for vulnerabilities (SQLi, brute force, IDOR, etc.).
- **Crawl and passively/actively scan** an app for common vulnerabilities (Pro only for the automated scanner).
- **Decode/encode data** (Base64, URL, hex, hashes) and diff two responses side by side.
- **Extend functionality** with plugins (BApp Store) for things like JWT manipulation, GraphQL testing, etc.

In short: **it's the tool you use to actually talk to and manipulate a web application at the raw HTTP level**, instead of just clicking around in the browser.

---

## How It Works (Under the Hood)

```
Your Browser  →  Burp Proxy (127.0.0.1:8080)  →  Target Web Server
                        ↑
              You see/edit traffic here
```

1. Your browser is configured to send all traffic through Burp's local proxy listener (default `127.0.0.1:8080`).
2. Burp receives the request first. Depending on settings, it either:
   - **Intercepts it** — pauses it so you can inspect/edit it before it goes out, or
   - **Passes it through** — logs it in the **HTTP History** but lets it continue automatically.
3. The response from the server comes back through Burp the same way, and gets logged too.
4. Because HTTPS is encrypted, Burp acts as a **man-in-the-middle with its own CA certificate** — you install Burp's certificate in your browser so it can decrypt, show you, and re-encrypt HTTPS traffic without your browser throwing certificate errors.
5. Every captured request can be sent to other Burp tools (Repeater, Intruder, etc.) with one click for further testing.

---

## Setting It Up

### 1. Install
Download from `portswigger.net/burp` (Community edition is free) — available for Linux/Windows/macOS, or on Kali it's pre-installed.

### 2. Configure your browser to use Burp's proxy
- Set browser proxy to `127.0.0.1:8080` (Burp's default listener), or use **FoxyProxy** extension to toggle it quickly.
- Best practice: use a dedicated browser profile just for Burp testing so you're not proxying your normal browsing.

### 3. Install Burp's CA certificate (for HTTPS)
- With the proxy active, visit `http://burp` in the proxied browser → download the CA certificate.
- Import it into your browser's trusted certificate store (Firefox: Settings → Certificates → Import; needed so HTTPS sites don't throw warnings).

---

## The Main Tools (Tabs)

### Proxy
Where it all starts. Shows **HTTP History** of every request/response. Toggle **Intercept is on/off** to pause live traffic for editing.

```
Proxy → Intercept → forward/drop/edit the request
Proxy → HTTP History → review everything that's passed through
```

### Target
Shows a **site map** — the tree of URLs/endpoints discovered as you browse through the proxy. Right-click any host → **"Add to scope"** to focus only on your authorized target and filter out noise (ads, analytics, etc.).

### Repeater
Send a single captured request here to **manually resend it again and again with edits** — the bread-and-butter tool for manual testing.
```
Workflow: Proxy → right-click request → "Send to Repeater" → tweak params → click Send → inspect response
```
Used for: testing parameter tampering, SQLi payloads one at a time, checking how the app responds to edge-case input.

### Intruder
**Automates sending many variations of a request** — define "payload positions" in the request, load a wordlist, and Burp fires it repeatedly, showing you response length/status/timing to spot anomalies.
```
Workflow: Send request to Intruder → mark payload position with § § → choose attack type → load payload list (wordlist) → Start attack
```
Attack types:
| Type | Behavior |
|---|---|
| **Sniper** | One payload set, cycles through one position at a time |
| **Battering ram** | Same payload inserted into all positions simultaneously |
| **Pitchfork** | Multiple payload sets, one per position, sent in parallel (position 1 gets list 1 item 1, position 2 gets list 2 item 1, etc.) |
| **Cluster bomb** | Multiple payload sets, every combination tried (good for user+pass brute force) |

Used for: brute-forcing logins, fuzzing parameters for injection points, enumerating valid usernames/IDs.

> [!note] Community edition limitation
> Intruder is heavily throttled (rate-limited) in the free version — usable for learning, painfully slow for real engagements.

### Decoder
Encode/decode data on the fly — Base64, URL encoding, HTML entities, hex, and hashing (MD5, SHA-1, etc.). Useful when you spot an encoded parameter and want to read/modify it.

### Comparer
Diffs two responses (or requests) side by side — great for spotting subtle differences, e.g. comparing a valid login response vs. an invalid one to find a behavioral tell.

### Sequencer
Analyzes the **randomness/entropy of tokens** (session IDs, CSRF tokens, password reset tokens) to check if they're predictable enough to be guessed/brute-forced.

---

## A Typical Manual Testing Workflow

```
1. Start Burp, configure browser proxy + install CA cert
2. Browse the target app normally through the proxied browser
   → Burp's Proxy/Target tabs fill in with every request made
3. Add the target's domain to Scope (Target tab) to reduce noise
4. Turn on Intercept, log in / submit a form, and watch the raw request
5. Send interesting requests to Repeater
   → try changing parameters, removing auth headers, altering IDs (IDOR test)
6. Send a login/search/filter request to Intruder
   → fuzz for SQLi, brute force credentials, enumerate valid values
7. Use Decoder if you spot Base64/hex-looking data in a parameter
8. Use Comparer if two similar responses behave differently
9. (Pro) Run the automated Scanner across the scoped site for a broad pass
```

---

## What Burp Is Commonly Used to Find

| Vulnerability class | How Burp helps |
|---|---|
| SQL Injection | Repeater/Intruder — inject payloads into parameters, inspect responses/errors |
| IDOR (Insecure Direct Object Reference) | Repeater — change an ID in the request, see if you access another user's data |
| Broken authentication | Intruder — brute force login, Sequencer — check token randomness |
| XSS | Repeater — inject script payloads into params/fields, check reflection in response |
| Business logic flaws | Repeater — replay requests out of order, tamper with prices/quantities/roles |
| Missing rate limiting | Intruder — hammer an endpoint and see if it's ever blocked |
| Hidden/forgotten endpoints | Target site map + Proxy history while crawling |

---

## Tips

- Always keep your test scope tight — set **Target → Scope** and filter the Proxy history to it, or you'll drown in noise from ads/trackers.
- **Burp Suite Academy** (`portswigger.net/web-security`) is the official, free training platform built around Burp — it pairs perfectly with hands-on practice and covers vulnerability classes step by step.
- Save your project (Pro/Community both support this now) so you don't lose history between sessions.
- Community edition is genuinely enough to learn 90% of manual web testing — the Scanner and unthrottled Intruder are really the only things Pro adds.
