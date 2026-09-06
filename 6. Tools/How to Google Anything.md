---
tags: [productivity, osint, google-fu, cheatsheet]
---

# How to Google Anything the Right Way

A reference for getting precise results fast instead of scrolling through 5 pages of noise.

---

## 1. The Core Mindset

- **Think like the page you're looking for, not like a question.** Instead of "why is my wifi slow", search `wifi slow after router firmware update` — use words that would actually appear on the answer page.
- **Start broad, then narrow.** Run a short 2-4 word query first, look at what comes back, then add operators to cut the noise.
- **Put the most specific/unique term first.** Error codes, exact model numbers, exact function names — these narrow results faster than generic words.
- **Drop filler words.** Google mostly ignores "the", "how", "a" anyway — search `postgres connection refused docker` not "how do I fix the connection refused error in postgres running in docker".

---

## 2. Essential Search Operators

| Operator | What it does | Example |
|---|---|---|
| `"exact phrase"` | Matches the exact phrase, word order included | `"connection refused" postgres` |
| `-word` | Excludes a word from results | `jaguar speed -car` |
| `site:` | Restricts to one website/domain | `site:reddit.com best budget keyboard` |
| `-site:` | Excludes a website | `python tutorial -site:w3schools.com` |
| `filetype:` | Restricts to a file type | `annual report 2025 filetype:pdf` |
| `intitle:` | Word must be in the page title | `intitle:"index of" backup` |
| `inurl:` | Word must be in the URL | `inurl:admin login` |
| `intext:` | Word must be in the page body | `intext:"api_key"` |
| `*` | Wildcard — fills in the unknown word | `"best * for beginners"` |
| `OR` (caps) | Either term can match | `python OR javascript tutorial` |
| `AND` (caps) | Both terms must match (default behavior, rarely needed explicitly) | `django AND celery` |
| `..` | Number range | `laptop $500..$800` |
| `related:` | Finds sites similar to a given one | `related:github.com` |
| `define:` | Quick dictionary definition | `define:latency` |
| `cache:` | Shows Google's last cached version of a page | `cache:example.com` |

> [!tip] Combine operators
> `site:stackoverflow.com intitle:"connection refused" postgres` finds Stack Overflow threads specifically about that error.

---

## 3. Time & Freshness Filters

Use **Tools → Any time** dropdown (below the search bar) to filter by:
- Past hour / 24 hours — breaking news, live issues
- Past week/month — recent releases, active discussions
- Custom range — research on a specific period

You can also append this manually in the URL: `&tbs=qdr:w` (past week), `&tbs=qdr:m` (past month), `&tbs=qdr:y` (past year).

---

## 4. Searching for Specific Content Types

| Goal | Query pattern |
|---|---|
| Find a PDF/report | `keyword filetype:pdf` |
| Find a forum discussion, not a blog spam site | `keyword site:reddit.com OR site:stackoverflow.com` |
| Find official docs only | `keyword site:docs.python.org` |
| Find code examples | `"function_name(" site:github.com` |
| Find a specific error, ignore SEO spam | `"exact error text" -site:pinterest.com -site:quora.com` |
| Find recent research papers | `keyword filetype:pdf site:arxiv.org` |
| Find someone's public presence | `"Full Name" site:linkedin.com` |

---

## 5. Google Dorking (OSINT / Recon Use)

> [!warning] Only use on targets you're authorized to test, or for your own OSINT footprint checks.

| Dork | Finds |
|---|---|
| `site:target.com filetype:pdf` | Publicly indexed PDFs on a domain |
| `site:target.com intitle:"index of"` | Open directory listings |
| `site:target.com inurl:admin` | Admin login pages |
| `site:target.com ext:sql \| ext:env \| ext:log` | Exposed config/log/db files |
| `"target.com" filetype:xls OR filetype:csv` | Leaked spreadsheets referencing the domain |
| `intext:"password" filetype:log` | Logs that leaked credentials |
| `site:pastebin.com "target.com"` | Pastes mentioning the target (leaks, source code) |
| `site:target.com inurl:login OR inurl:signin` | Login endpoints |

For a big curated list, the **Google Hacking Database (GHDB)** on Exploit-DB is the standard reference: `exploit-db.com/google-hacking-database`

---

## 6. Fixing Bad Search Results

| Problem | Fix |
|---|---|
| Too many SEO/spam blogs | Add `-site:pinterest.com -site:quora.com` or target `site:reddit.com` |
| Results are outdated | Use the time filter (Section 3) |
| Getting synonyms instead of your exact term | Wrap it in `"quotes"` |
| Can't remember the exact phrase | Use `*` as a wildcard placeholder |
| Question is too vague to search well | Rewrite it as the phrase you'd expect in the answer, not as a question |
| Need info from a specific trustworthy source only | Use `site:` to restrict to it (docs, .gov, .edu) |

---

## 7. Quick Reference Card

```
"exact phrase"        → force exact match
-word                 → exclude word
site:example.com      → only this site
-site:example.com     → exclude this site
filetype:pdf          → only this file type
intitle:word          → word must be in title
inurl:word            → word must be in URL
word1 OR word2        → either term
term..term            → number range
```
