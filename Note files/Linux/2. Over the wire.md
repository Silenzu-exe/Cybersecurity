---

## tags: [cybersecurity, overthewire, bandit, linux, ctf] status: in-progress started:

# OverTheWire — Bandit Wargame

> [!info] Connection info Connect to each level with:
> 
> ```bash
> ssh banditN@bandit.labs.overthewire.org -p 2220
> ```
> 
> Replace `N` with the level number, and use the password found from the previous level.

---

## Level 0 → 1

> [!question] Goal Log into the game using SSH. Host: `bandit.labs.overthewire.org`, Port: `2220`. Username `bandit0`, password `bandit0`.

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

**Password for bandit1:** `(starting password is bandit0)`

---

## Level 1 → 2

> [!question] Goal The password for the next level is stored in a file called `-` located in the home directory.

`-` is interpreted by most commands as "read from stdin", so it has to be referenced as `./-`.

```bash
cat ./-
```

**Password for bandit2:** `<paste here>`

---

## Level 2 → 3

> [!question] Goal The password for the next level is stored in a file called `spaces in this filename` located in the home directory.

Spaces need to be escaped or the filename quoted.

```bash
cat "spaces in this filename"
# or
cat spaces\ in\ this\ filename
```

**Password for bandit3:** `<paste here>`

---

## Level 3 → 4

> [!question] Goal The password for the next level is stored in a hidden file in the `inhere` directory.

```bash
cd inhere
ls -la              # list hidden files
cat ./...filename   # display the content of the hidden file
```

**Password for bandit4:** `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

---

## Level 4 → 5

> [!question] Goal The password for the next level is stored in the only human-readable file in the `inhere` directory.

```bash
file ./*            # shows file types — find the "ASCII text" one
cat ./-file07
```

**Password for bandit5:** `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

> [!note] Linux permission digits `7` = read+write+execute, `4` = read, `1` = execute (sum of `r=4, w=2, x=1`).

---

## Level 5 → 6

> [!question] Goal The password for the next level is stored somewhere under the `inhere` directory and has **all** of these properties: human-readable, **1033 bytes** in size, **not executable**.

```bash
find . -size 1033c -type f ! -executable
```

- `find .` — search current directory and subdirectories
- `-type f` — files only (not directories)
- `-size 1033c` — exactly 1033 bytes (`c` = bytes)
- `! -executable` — not executable

**Password for bandit6:** `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

---

## Level 6 → 7

> [!question] Goal The password for the next level is stored **somewhere on the server** and has all of these properties: owned by user `bandit7`, owned by group `bandit6`, **33 bytes** in size.

```bash
find / -size 33c -user bandit7 -group bandit6 2>/dev/null
```

- `find /` — search from root directory
- `-user bandit7` — owned by user bandit7
- `-group bandit6` — owned by group bandit6
- `-size 33c` — exactly 33 bytes
- `2>/dev/null` — suppress "permission denied" noise

**Password for bandit7:** `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

---

## Level 7 → 8

> [!question] Goal The password for the next level is stored in the file `data.txt` next to the word `millionth`.

```bash
grep "millionth" data.txt
```

`grep` searches for a specific pattern/text inside a file.

**Password for bandit8:** `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

---

## Level 8 → 9

> [!question] Goal The password for the next level is stored in `data.txt` and is the **only line of text that occurs only once**.

```bash
sort data.txt | uniq -u
```

- `sort` — sorts the lines alphabetically (required before `uniq` can compare neighbours)
- `uniq -u` — prints only the lines that are unique (appear exactly once)
- `|` — pipes the sorted output into `uniq`

**Password for bandit9:** `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

---

## Level 9 → 10

> [!question] Goal The password for the next level is stored in `data.txt`, in one of the few human-readable strings, **preceded by several `=` characters**.

```bash
strings data.txt | grep "^="
```

`strings` extracts printable character sequences from a binary file — useful when the file is mostly non-text data.

**Password for bandit10:** `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`

---

## Level 10 → 11

> [!question] Goal The password for the next level is stored in `data.txt`, which contains **base64-encoded** data.

```bash
base64 -d data.txt
```

> [!note] What is Base64?
> 
> - Binary-to-text encoding scheme
> - Converts binary data into ASCII text
> - Uses 64 characters (A–Z, a–z, 0–9, `+`, `/`) plus `=` for padding
> - Common in email attachments, data URLs, storing binary data as text
> 
> **Useful flags**
> 
> - `base64 -d` / `base64 --decode` — decode base64
> - `base64` (no flag) — encode to base64
> - `-w 0` — disable line wrapping (useful when encoding)
> - `-i` — ignore non-alphabet characters

**Password for bandit11:** `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`

---

## Level 11 → 12

> [!question] Goal The password for the next level is stored in `data.txt`, where all lowercase (a-z) and uppercase (A-Z) letters have been **rotated by 13 positions** (ROT13).

```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

> [!note] What is ROT13?
> 
> - "Rotate by 13 places" — a simple substitution cipher
> - Replaces each letter with the one 13 positions ahead
> - Self-inverse: applying ROT13 twice returns the original text
> - Example: ROT13(A) = N, ROT13(B) = O, ROT13(C) = P …
> 
> **How the `tr` mapping works**
> 
> - `'A-Za-z'` — all uppercase and lowercase letters (the "from" set)
> - `'N-ZA-Mn-za-m'` — maps A→N, B→O, …, Z→M, and the same pattern for lowercase

**Password for bandit12:** `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`

---

## Level 12 → 13

> [!question] Goal The password for the next level is stored in `data.txt`, which is a **hexdump of a file that has been repeatedly compressed**. (Tip: work inside a scratch directory under `/tmp`, e.g. made with `mktemp -d`.)

```bash
# (solution not yet documented — in progress)
```

**Password for bandit13:** `FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn`

---

## 🧰 Command Cheat Sheet (so far)

| Command                                        | Purpose                                         |
| ---------------------------------------------- | ----------------------------------------------- |
| `ls -la`                                       | list all files, including hidden                |
| `find . -size Nc -type f`                      | find files of exact byte size                   |
| `find / -user X -group Y -size Nc 2>/dev/null` | find files by owner/group/size, suppress errors |
| `grep "text" file`                             | search for a string inside a file               |
| `sort file \| uniq -u`                         | find the line that appears exactly once         |
| `strings file`                                 | extract printable text from a binary file       |
| `base64 -d file`                               | decode base64 data                              |
| `tr 'A-Za-z' 'N-ZA-Mn-za-m'`                   | ROT13 encode/decode                             |
| `file ./*`                                     | show file type of everything in a directory     |

---

## 📌 Notes to self

- Always note the password before logging out — they aren't saved automatically.
- Passwords can change over time on the live server; commands/technique matter more than memorizing exact strings.
- Next up: Level 13 (hexdump + repeated compression), then SSH keys, ports, and cronjobs in later levels.






