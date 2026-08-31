---
tags: [networking, cybersecurity, http, https, cheatsheet]
---

# 04 — HTTP & HTTPS

---

## What is HTTP?

HTTP (HyperText Transfer Protocol), developed by Tim Berners-Lee between 1989–1991, is the set of rules used to communicate with web servers to transmit webpage data — HTML, images, video, etc.

## What is HTTPS?

HTTPS (HyperText Transfer Protocol Secure) is the encrypted version of HTTP. It stops people from reading the data in transit, and also assures you that you're talking to the real server, not an impersonator.

| | HTTP | HTTPS |
|---|---|---|
| Port | 80 | 443 |
| Encryption | None (plaintext) | TLS/SSL |
| Intercept risk | High — anyone on the network can read it | Encrypted in transit |

---

## Anatomy of a URL

A URL (Uniform Resource Locator) tells the browser how and where to access a resource.

```
http://user:password@tryhackme.com:80/view-room?id=1#task3
```

| Part | Example | Meaning |
|---|---|---|
| **Scheme** | `http` | Protocol to use (HTTP, HTTPS, FTP, etc.) |
| **User** | `user:password` | Optional credentials for services requiring login via URL |
| **Host** | `tryhackme.com` | Domain name or IP of the server |
| **Port** | `80` | Port to connect to (80 default HTTP, 443 default HTTPS, but can be 1–65535) |
| **Path** | `/view-room` | File name/location of the resource |
| **Query string** | `?id=1` | Extra data sent to the path (e.g. blog article id) |
| **Fragment** | `#task3` | Reference to a location within the page itself |

---

## Making a Request

The simplest possible request is one line: `GET / HTTP/1.1`. For a real web experience, extra data is sent as **headers**.

**Example request:**
```http
GET / HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Referer: https://tryhackme.com/
```
- Line 1: GET method, requesting `/` (home page), using HTTP/1.1
- Line 2: which website (virtual hosting — one server can host multiple domains)
- Line 3: which browser/version is making the request
- Line 4: which page referred us here
- A blank line always ends an HTTP request

**Example response:**
```http
HTTP/1.1 200 OK
Server: nginx/1.15.8
Date: Fri, 09 Apr 2021 13:34:03 GMT
Content-Type: text/html
Content-Length: 98

<html>
<head><title>TryHackMe</title></head>
<body>Welcome To TryHackMe.com</body>
</html>
```
- Line 1: HTTP version + status code (`200 OK` = success)
- Line 2: server software/version
- Line 3: date/time/timezone of the server
- Line 4: content type being sent (HTML, image, video, PDF, etc.)
- Line 5: content length, so the client can confirm nothing is missing
- Blank line ends the header section, followed by the actual body

---

## HTTP Methods

| Method | Purpose | Security note |
|---|---|---|
| **GET** | Retrieve a resource | Params in the URL — logged everywhere (browser history, server logs) |
| **POST** | Submit data / create new records | Body hidden from the URL, but not encrypted without HTTPS |
| **PUT** | Update/replace a resource | Often abused if server is misconfigured |
| **DELETE** | Delete a resource/record | Should require auth — often doesn't |
| **OPTIONS** | Lists allowed methods | Can reveal attack surface |
| **PATCH** | Partial update | |

---

## HTTP Status Codes

Grouped into 5 ranges:

| Range | Meaning |
|---|---|
| **100–199** | Informational — request accepted so far, continue sending (rare today) |
| **200–299** | Success |
| **300–399** | Redirection — to another resource or site |
| **400–499** | Client error |
| **500–599** | Server error — often a major backend problem |

**Common codes:**

| Code | Meaning | Security relevance |
|---|---|---|
| **200** OK | Request completed successfully | Normal response |
| **201** Created | A resource was created (new user, new post) | |
| **301** Moved Permanently | Redirects browser/search engines to a new location | Redirects can be hijacked |
| **302** Found | Temporary redirect | Redirects can be hijacked |
| **400** Bad Request | Something was wrong/missing in the request | Input parsing error |
| **401** Not Authorised | Must authenticate first | Auth required |
| **403** Forbidden | No permission, whether logged in or not | You're blocked but the resource exists |
| **404** Not Found | Resource doesn't exist | |
| **405** Method Not Allowed | Resource doesn't accept this method (e.g. GET on a POST-only endpoint) | |
| **500** Internal Server Error | Server hit an error handling the request | Can leak stack traces/version info |
| **503** Service Unavailable | Server overloaded or down for maintenance | May indicate a DoS in progress |

---

## Security Relevance

- Everything in plain HTTP (URLs, cookies, POST bodies) can be sniffed on the network — see [[08_Packet_Analysis]].
- Most web application attacks (SQLi, XSS, CSRF, auth bypass) happen at this layer — see [[01_OSI_and_TCPIP_Model]] for where this sits in the stack.
- Directory/endpoint discovery tools (`gobuster`, `nikto`, `whatweb`) rely on interpreting status codes and headers — see [[07_Nmap_and_Recon]].
