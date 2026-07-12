
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

## OpenSSL: 


To encrypt our file, we'll use this OpenSSL command:

```bash
openssl enc -aes-256-cbc -salt -in secret.txt -out secret.enc -pbkdf2
```

Here's what each part does:

	openssl enc: Invokes OpenSSL's encryption function
    -aes-256-cbc: Specifies our chosen encryption method
    -salt: Adds random data to prevent identical messages from looking the same when encrypted
    -in secret.txt: Names our input file containing the original message
    -out secret.enc: Specifies where to save the encrypted output
    -pbkdf2: Uses Password-Based Key Derivation Function 2 to securely generate encryption keys from passwords
    
```
```
To decrypt our encrypted file we use, 

```bash
openssl enc -aes-256-cbc -d -in secret.enc -out decrypted.txt -pbkdf2
```

## Nmap: 

**TCP connect scan:**
```bash
namp -sT -p 8000 localhost
```
-  -sT is an option that specifies a TCP connect scan. This tells Nmap to use the TCP connect method to check the status of the ports.
- -p 8000 indicates that we want Nmap to scan only port 8000. You can change this number to scan other ports if needed.
- localhost is the target of our scan. It refers to the local machine where the service is running.

**More detail scanning: **
```bash
namp -sV -p 8000 localhost
```
- The `-sV` option is used to tell Nmap to probe open ports to determine service/version information. This means Nmap will try to figure out what specific software and version is running on the open port.

** Scanning multiple ports: **

```bash
nmap localhost #scan 1000 common ports

nmap -p- localhost #scans all 65535 TCP/IP ports
```
- This command, without any port specification, will scan the top 1000 most common ports. You should see a list of open, closed, and filtered ports. The output shows the port number, its state (open, closed, or filtered), and the associated service.

- Now, let's scan all 65535 ports. In the TCP/IP protocol, there are a total of 65535 ports available. Scanning all of them can give you a complete picture of the services running on the target, but it takes more time.

```bash
nmap -p 1-1000 localhost
```
- This command scans ports 1 through 1000. By specifying a port range, you can focus your scan on the ports that are most relevant to your needs.

**Output format and Saving Results: **

1. Normal format
```bash
namp -oN normal.txt localhost 
```
- In this command, the `-oN` option is used to instruct Nmap to save the output in normal format. The `normal_output.txt` is the name of the file where the results will be stored. The `localhost` is the target we are scanning, which refers to the local machine itself.

2. XML format

```bash 
nmap -oX xml_output.xml localhost
```
- Here, the `-oX` option tells Nmap to save the output in XML format. The `xml_output.xml` is the file where the XML - formatted results will be saved.

3. Grepable format:
```bash
nmap -oG greapable.txt localhost
```
- The `-oG` option is used to save the output in grepable format, and the `grepable_output.txt` is the file where the results will be stored.

---


## Nmap basic syntax: 

**Netcat (nc):** 

```bash
nc -h
while true; do nc -n -lvp 7777; done
```
- - `n`: This flag tells netcat to use IP addresses directly instead of trying to resolve hostnames. It speeds up the process and avoids potential DNS - related issues.
- `-l`: This flag tells netcat to enter listening mode. It waits for incoming connections instead of trying to initiate them.
- `-v`: This flag enables verbose output. Netcat will provide more detailed information about what it's doing, which is helpful for debugging and understanding what's happening.
- `-p 7777`: This flag specifies the port number on which netcat should listen. In this case, we've chosen port 7777.

**locate the serever with the namp:**

```bash
nmap -v -p 7777 localhost
```

- `nmap`: This is the base command to run Nmap. It tells the system that we want to use the Nmap tool for network scanning.
- `-v`: This option enables verbose output. When we use `-v`, Nmap will give us more detailed information about the scan, such as the progress and additional details about the target.
- `-p 7777`: This option tells Nmap to scan only port 7777. Ports are like doors on a computer, and different services use different ports. By specifying `-p 7777`, we are asking Nmap to check if port 7777 is open on the target machine.
- `localhost`: This is the target we want to scan. In this case, `localhost` refers to your own machine. It's a way to test the network scanning on your local environment.