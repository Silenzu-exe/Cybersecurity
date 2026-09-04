
>[!note] This file contains the syntax and information about the tools used in `LabEX` and other `E-learning platform`.
## Hydra:

**Hydra** is an open source password brute-forcing tool designed for **online brute-
force attacks** against network protocols. Hydra can perform rapid dictionary attacks against more than 50 protocols including telnet, FTP, HTTP, HTTPS, SMB, databases, and several other services.

```bash
hydra -l securityadmin -P passwords.txt localhost -s 8080 http-post-form "/:username=^USER^&password=^PASS^:invalid username or password" -o hydra_result.txt

# -l single username
# -L Username file
# -p single password
# -P password file
# -s specify port
# http-post-form : attacking web login forms using HTTP POST method with placeholders ^USER^ and ^PASS^.
# -o store output
```


