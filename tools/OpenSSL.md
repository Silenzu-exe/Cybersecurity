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
