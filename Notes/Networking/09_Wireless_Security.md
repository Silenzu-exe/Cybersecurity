---
tags: [networking, cybersecurity, wireless, wifi, cheatsheet]
---

# 09 — Wireless Security

> [!note] Termux limitation
> Most WiFi attacks (monitor mode, packet injection) require a USB WiFi adapter that supports monitor mode + a compatible kernel driver. Android's built-in WiFi stack blocks this. The commands here are for a Linux machine with a compatible adapter — not Termux on your phone. The concepts apply everywhere.

---

## WiFi Security Protocols (Chronological)

| Protocol | Year | Status | Why it matters |
|---|---|---|---|
| **WEP** | 1997 | **Broken** — never use | RC4 cipher misused; crackable in minutes with enough packets |
| **WPA** | 2003 | **Deprecated** | Interim fix for WEP flaws; also vulnerable |
| **WPA2** | 2004 | Still widely used | AES-based; secure if strong passphrase. KRACK attack (2017) is a concern but requires local position |
| **WPA3** | 2018 | Current standard | SAE handshake replaces PSK; resistant to offline dictionary attacks |

---

## WPA2 Authentication Modes

| Mode | Full name | Used where | How it works |
|---|---|---|---|
| **WPA2-Personal (PSK)** | Pre-Shared Key | Home/small office | Everyone uses the same password |
| **WPA2-Enterprise** | 802.1X/EAP | Corporate | Individual credentials; RADIUS server authentication |

---

## WPS (Wi-Fi Protected Setup)

**What:** Easier way to connect devices without typing the full password (PIN or push-button).

> [!warning] Security issue
> WPS PIN mode is fundamentally broken — the 8-digit PIN is effectively 11,000 combinations (split into two halves checked independently). Tools like `reaver` and `bully` can crack it in hours.
> **Best practice:** Disable WPS entirely.

---

## The 4-Way Handshake (WPA2-PSK)

This is what tools capture to crack WPA2:

```
AP → Client:  EAPOL Message 1 (ANonce)
Client → AP:  EAPOL Message 2 (SNonce + MIC)
AP → Client:  EAPOL Message 3 (GTK + MIC)
Client → AP:  EAPOL Message 4 (ACK)
```

The attacker captures this handshake, then tries to derive the PSK offline using dictionary/brute force. The actual PSK is **never transmitted** — but if the attacker guesses it, they can validate it against the captured MIC.

---

## Key Terms

| Term | Meaning |
|---|---|
| SSID | Network name (broadcasted in beacon frames) |
| BSSID | MAC address of the access point |
| Channel | WiFi frequency channel (1-13 for 2.4GHz) |
| Monitor mode | Adapter mode for capturing all nearby WiFi traffic (not just your own) |
| Packet injection | Ability to forge and send arbitrary WiFi frames |
| Beacon frame | AP broadcasts this regularly to announce its existence |
| Probe request | Client broadcasts looking for known networks |
| Deauth frame | Forces a client to disconnect — used to capture 4-way handshake |
| PMKID | An alternative to capturing the full 4-way handshake (WPA2 cracking) |
| KRACK | Key Reinstallation Attack — 2017 WPA2 vulnerability |
| SSID hiding | Hiding the network name — security through obscurity; easily defeated |

---

## Common WiFi Attacks

### Evil Twin / Rogue AP
Attacker creates a fake AP with the same SSID as the target — clients auto-connect to the stronger signal, then MITM.

**What it enables:** Capture credentials, inject malicious content, SSL strip.

### Deauthentication Attack
Send spoofed deauth frames (no auth required in 802.11 — this is by design) to kick a client off the network. Used to:
1. Force client to reconnect → capture the 4-way handshake
2. DoS — keep kicking a client

WPA3 and 802.11w (Protected Management Frames) fix this.

### WPA2 Handshake Capture + Offline Crack
1. Get into monitor mode
2. Capture a 4-way handshake (or force one with deauth)
3. Run offline dictionary attack against the captured handshake
4. If password is in the wordlist, you crack it

**Tools (on a full Linux system):** `aircrack-ng`, `hashcat` (GPU-accelerated), `hcxtools`

### WPA2 PMKID Attack
Newer method — doesn't require capturing a handshake or even waiting for a client to connect. Extracts PMKID from the AP directly.

**Tools:** `hcxdumptool`, `hcxtools`, `hashcat`

---

## Wireless Recon Commands (Linux with compatible adapter)

```bash
# Put adapter into monitor mode
sudo airmon-ng start wlan0
# Creates wlan0mon (monitor interface)

# Scan for nearby networks
sudo airodump-ng wlan0mon

# Focus on a specific network + capture handshake
sudo airodump-ng -c [channel] --bssid [AP_MAC] -w capture wlan0mon

# Deauth a client to force handshake (separate terminal)
sudo aireplay-ng --deauth 5 -a [AP_MAC] -c [CLIENT_MAC] wlan0mon

# Crack captured handshake with wordlist
aircrack-ng capture.cap -w /usr/share/wordlists/rockyou.txt

# Back to managed mode when done
sudo airmon-ng stop wlan0mon
```

---

## Defense Checklist

```
[ ] Use WPA3 if router supports it; WPA2-PSK minimum
[ ] Use a strong, long WiFi password (20+ chars, random)
[ ] Disable WPS
[ ] Enable 802.11w (Protected Management Frames) if available
[ ] Disable remote management / UPnP on router
[ ] Keep router firmware updated
[ ] Use WPA2-Enterprise (RADIUS) for corporate environments
[ ] Don't trust open WiFi — use VPN
[ ] Check for rogue APs on corporate networks with a WIDS
```

---

## What "Securing" a Wireless Network Actually Involves

| Layer | What to address |
|---|---|
| Authentication | Strong PSK or 802.1X Enterprise |
| Protocol | WPA3 (or WPA2 + strong password as minimum) |
| Management frames | Enable PMF (802.11w) |
| Physical | AP placement; signal doesn't need to reach outside the building |
| Monitoring | Wireless IDS to detect rogue APs, deauth floods |
| Segmentation | Guest VLAN isolated from internal network |
