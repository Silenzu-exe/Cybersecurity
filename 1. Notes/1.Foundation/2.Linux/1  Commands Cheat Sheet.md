# Linux Commands

A comprehensive guide to essential Linux commands organized by topic with practical examples.

---

## Navigation & Directory Commands

### pwd (Print Working Directory)
Show current directory location
```bash
pwd
# Output: /home/username/documents
```

### ls (List)
List files and directories
```bash
# Basic list
ls

# Detailed list with permissions, size, date
ls -l

# Show hidden files (starting with .)
ls -a

# Human-readable file sizes
ls -lh

# Sort by modification time (newest first)
ls -lt

# Reverse order
ls -lr

# Combined options
ls -lah
```

### cd (Change Directory)
Navigate between directories
```bash
# Go to specific directory
cd /home/username/documents

# Go to home directory
cd ~
cd

# Go up one directory
cd ..

# Go up two directories
cd ../..

# Go to previous directory
cd -

# Go to root directory
cd /
```

### mkdir (Make Directory)
Create new directories
```bash
# Create single directory
mkdir new_folder

# Create multiple directories
mkdir folder1 folder2 folder3

# Create nested directories (parent + child)
mkdir -p parent/child/grandchild

# Create with specific permissions
mkdir -m 755 secure_folder
```

### rmdir (Remove Directory)
Remove empty directories
```bash
# Remove empty directory
rmdir empty_folder

# Remove nested empty directories
rmdir -p parent/child/grandchild
```

---

## Basic File Operations

### touch
Create empty files or update timestamps
```bash
# Create new empty file
touch newfile.txt

# Create multiple files
touch file1.txt file2.txt file3.txt

# Update modification time of existing file
touch existing_file.txt
```

### cat (Concatenate)
Display file contents
```bash
# Display file content
cat file.txt

# Display multiple files
cat file1.txt file2.txt

# Display with line numbers
cat -n file.txt

# Create new file with content (Ctrl+D to save)
cat > newfile.txt
This is content
Press Ctrl+D to save

# Append to existing file
cat >> existing_file.txt
More content
Press Ctrl+D to save

# Combine files into new file
cat file1.txt file2.txt > combined.txt
```

### cp (Copy)
Copy files and directories
```bash
# Copy file
cp source.txt destination.txt

# Copy file to directory
cp file.txt /home/username/documents/

# Copy multiple files to directory
cp file1.txt file2.txt file3.txt /target/directory/

# Copy directory (recursive)
cp -r source_folder/ destination_folder/

# Copy with confirmation prompt
cp -i source.txt destination.txt

# Copy preserving attributes (permissions, timestamps)
cp -p source.txt destination.txt

# Verbose output (show what's being copied)
cp -v source.txt destination.txt
```

### mv (Move/Rename)
Move or rename files and directories
```bash
# Rename file
mv oldname.txt newname.txt

# Move file to directory
mv file.txt /home/username/documents/

# Move multiple files
mv file1.txt file2.txt file3.txt /target/directory/

# Move directory
mv old_folder/ new_folder/

# Move with confirmation prompt
mv -i source.txt destination.txt

# Don't overwrite existing files
mv -n source.txt destination.txt
```

### rm (Remove)
Delete files and directories
```bash
# Remove file
rm file.txt

# Remove multiple files
rm file1.txt file2.txt file3.txt

# Remove with confirmation
rm -i file.txt

# Remove directory and contents (recursive)
rm -r folder/

# Force remove (no confirmation)
rm -f file.txt

# Force remove directory
rm -rf folder/

# Verbose output
rm -v file.txt

# Remove all .txt files
rm *.txt
```

⚠️ **Warning:** `rm -rf` is dangerous! It permanently deletes without confirmation.

---

## File Viewing & Editing

### more
View file content page by page
```bash
# View file
more file.txt

# Space = next page
# Enter = next line
# q = quit
```

### less
Advanced file viewer (better than more)
```bash
# View file
less file.txt

# Space/PgDn = next page
# PgUp = previous page
# / = search forward
# ? = search backward
# q = quit
# G = go to end
# g = go to beginning
```

### head
View beginning of file
```bash
# Show first 10 lines (default)
head file.txt

# Show first 20 lines
head -n 20 file.txt

# Show first 50 bytes
head -c 50 file.txt
```

### tail
View end of file
```bash
# Show last 10 lines (default)
tail file.txt

# Show last 20 lines
tail -n 20 file.txt

# Follow file in real-time (useful for logs)
tail -f /var/log/syslog

# Follow with line count
tail -n 50 -f logfile.log
```

### nano
Simple text editor
```bash
# Open/create file
nano file.txt

# Keyboard shortcuts:
# Ctrl+O = Save
# Ctrl+X = Exit
# Ctrl+K = Cut line
# Ctrl+U = Paste
# Ctrl+W = Search
```

### vim
Advanced text editor
```bash
# Open file
vim file.txt

# Basic commands:
# i = Insert mode (start typing)
# Esc = Command mode
# :w = Save
# :q = Quit
# :wq = Save and quit
# :q! = Quit without saving
# dd = Delete line
# yy = Copy line
# p = Paste
```

---

## File Permissions

### Understanding Permissions
```
-rwxr-xr--
│││││││││└─ Others: read
││││││││└── Others: no write
│││││││└─── Others: no execute
││││││└──── Group: read
│││││└───── Group: no write
││││└────── Group: execute
│││└─────── Owner: read
││└──────── Owner: write
│└───────── Owner: execute
└────────── File type (- = file, d = directory, l = link)
```

**Permission Numbers:**
- `r (read) = 4`
- `w (write) = 2`
- `x (execute) = 1`

**Common Permission Combinations:**
- `7 = 4+2+1 = rwx`
- `6 = 4+2 = rw-`
- `5 = 4+1 = r-x`
- `4 = 4 = r--`
- `0 = ---`

### chmod (Change Mode)
Change file permissions
```bash
# Using numbers (rwx = 7, rw- = 6, r-x = 5, r-- = 4)
chmod 755 file.txt    # rwxr-xr-x (owner: all, group/others: read+execute)
chmod 644 file.txt    # rw-r--r-- (owner: read+write, group/others: read only)
chmod 777 file.txt    # rwxrwxrwx (everyone: all permissions)
chmod 600 file.txt    # rw------- (owner: read+write only)

# Using symbols
chmod u+x file.txt    # Add execute for owner (user)
chmod g+w file.txt    # Add write for group
chmod o-r file.txt    # Remove read for others
chmod a+r file.txt    # Add read for all (user+group+others)

# Recursive (apply to directory and contents)
chmod -R 755 folder/

# u = user/owner
# g = group
# o = others
# a = all
# + = add permission
# - = remove permission
# = = set exact permission
```

**Common Permission Examples:**
```bash
# Executable script
chmod +x script.sh
chmod 755 script.sh

# Private file (only you can read/write)
chmod 600 private.txt

# Public readable directory
chmod 755 public_folder/

# Shared directory for group
chmod 775 shared_folder/

# Web files
chmod 644 index.html    # Files
chmod 755 cgi-bin/      # Directories
```

---

## File Ownership

### chown (Change Owner)
Change file owner and group
```bash
# Change owner
sudo chown username file.txt

# Change owner and group
sudo chown username:groupname file.txt

# Change only group
sudo chown :groupname file.txt

# Recursive (directory and contents)
sudo chown -R username:groupname folder/

# Examples:
sudo chown john document.txt
sudo chown john:developers project/
sudo chown -R www-data:www-data /var/www/html/
```

### chgrp (Change Group)
Change file group ownership
```bash
# Change group
sudo chgrp groupname file.txt

# Recursive
sudo chgrp -R developers project/

# Example:
sudo chgrp www-data /var/www/index.html
```

---

## File Search & Find

### find
Search for files and directories
```bash
# Find by name
find /home -name "file.txt"

# Find by name (case-insensitive)
find /home -iname "FILE.txt"

# Find all .txt files
find . -name "*.txt"

# Find directories only
find . -type d

# Find files only
find . -type f

# Find by size (larger than 10MB)
find . -size +10M

# Find by size (smaller than 1MB)
find . -size -1M

# Find modified in last 7 days
find . -mtime -7

# Find modified more than 30 days ago
find . -mtime +30

# Find and delete
find . -name "*.tmp" -delete

# Find and execute command
find . -name "*.txt" -exec cat {} \;

# Find with permissions
find . -perm 644

# Find empty files
find . -empty

# filter error output
2>dev/null    #(write in the last of the code)
```

### grep
Search text within files
```bash
# Search for text in file
grep "search_term" file.txt

# Case-insensitive search
grep -i "search_term" file.txt

# Search in multiple files
grep "error" *.log

# Recursive search in directory
grep -r "TODO" /home/project/

# Show line numbers
grep -n "error" file.txt

# Show only filenames with match
grep -l "error" *.log

# Show count of matches
grep -c "error" file.txt

# Invert match (lines NOT containing term)
grep -v "success" file.txt

# Search with regular expressions
grep "^Error" file.txt    # Lines starting with "Error"
grep "ERROR$" file.txt    # Lines ending with "ERROR"

# Multiple patterns
grep -E "error|warning|critical" file.txt

# Search with context (show 2 lines before and after)
grep -C 2 "error" file.txt
```

### locate
Quick file search using database
```bash
# Find file by name
locate file.txt

# Case-insensitive
locate -i FILE.txt

# Update database (run before searching new files)
sudo updatedb

# Limit results
locate -n 5 file.txt
```

### which
Find location of executable
```bash
# Find where command is located
which python
which java
which node

# Output: /usr/bin/python
```

### whereis
Find binary, source, and manual page files
```bash
# Find all related files
whereis python

# Output: python: /usr/bin/python /usr/lib/python /usr/share/man/man1/python.1.gz
```
### String
Extract human readable format

```shell
# Filter human readable format
string filename.txt

# uniq -u filter unique one liner (sort)
sort filename | uniq -u 

```
---


## File Comparison & Differences

### diff
Compare files line by line
```bash
# Compare two files
diff file1.txt file2.txt

# Side-by-side comparison
diff -y file1.txt file2.txt

# Show differences in unified format
diff -u file1.txt file2.txt

# Ignore case
diff -i file1.txt file2.txt

# Compare directories
diff -r dir1/ dir2/
```

### cmp
Compare files byte by byte
```bash
# Compare files
cmp file1.txt file2.txt

# Show differences
cmp -l file1.txt file2.txt
```

---

## File Compression & Archives

### tar (Tape Archive)
Create and extract archives
```bash
# Create archive (.tar)
tar -cvf archive.tar folder/

# Create compressed archive (.tar.gz)
tar -czvf archive.tar.gz folder/

# Extract archive
tar -xvf archive.tar

# Extract compressed archive
tar -xzvf archive.tar.gz

# Extract to specific directory
tar -xzvf archive.tar.gz -C /target/directory/

# List contents without extracting
tar -tvf archive.tar

# c = create
# x = extract
# v = verbose
# f = file
# z = gzip compression
# j = bzip2 compression
```

### gzip
Compress files
```bash
# Compress file (creates file.gz, removes original)
gzip file.txt

# Decompress
gunzip file.txt.gz

# Keep original file
gzip -k file.txt

# Compress with specific level (1=fast, 9=best compression)
gzip -9 file.txt
```

### zip / unzip
Create and extract ZIP archives
```bash
# Create zip archive
zip archive.zip file1.txt file2.txt

# Create zip with directory
zip -r archive.zip folder/

# Extract zip
unzip archive.zip

# Extract to specific directory
unzip archive.zip -d /target/directory/

# List contents
unzip -l archive.zip
```

---

## System Information

### uname
System information
```bash
# Show all system info
uname -a

# Show kernel name
uname -s

# Show kernel version
uname -r

# Show machine hardware name
uname -m
```

### df (Disk Free)
Disk space usage
```bash
# Show disk usage
df

# Human-readable format
df -h

# Show specific filesystem
df -h /home
```

### du (Disk Usage)
Directory/file size
```bash
# Show directory size
du -sh folder/

# Show all files and folders with sizes
du -h folder/

# Show top 10 largest directories
du -h / | sort -rh | head -10

# s = summarize
# h = human-readable
```

### free
Memory usage
```bash
# Show memory usage
free

# Human-readable
free -h

# Show in megabytes
free -m
```

### top
Real-time system processes
```bash
# Show processes
top

# q = quit
# k = kill process
# M = sort by memory
# P = sort by CPU
```

### htop
Interactive process viewer (better than top)
```bash
# Show processes (if installed)
htop

# F9 = kill process
# F10 = quit
```

### ps (Process Status)
Show running processes
```bash
# Show current user processes
ps

# Show all processes
ps aux

# Show processes by user
ps -u username

# Show process tree
ps -ef --forest

# Find specific process
ps aux | grep python
```

---

## Network Commands

### ping
Test network connectivity
```bash
# Ping website
ping google.com

# Ping specific number of times
ping -c 4 google.com

# Stop: Ctrl+C
```

### curl
Transfer data from URLs
```bash
# Get webpage content
curl https://example.com

# Download file
curl -O https://example.com/file.zip

# Save with custom name
curl -o myfile.zip https://example.com/file.zip

# Follow redirects
curl -L https://example.com

# Show headers
curl -I https://example.com
```

### wget
Download files
```bash
# Download file
wget https://example.com/file.zip

# Download with custom name
wget -O myfile.zip https://example.com/file.zip

# Continue interrupted download
wget -c https://example.com/file.zip

# Download recursively
wget -r https://example.com/
```

### ifconfig
Network interface configuration
```bash
# Show network interfaces
ifconfig

# Show specific interface
ifconfig eth0

# Bring interface up
sudo ifconfig eth0 up

# Bring interface down
sudo ifconfig eth0 down
```

### ip
Modern network configuration
```bash
# Show all network interfaces
ip addr

# Show routing table
ip route

# Show specific interface
ip addr show eth0
```

---

## User & Group Management

### whoami
Show current username
```bash
whoami
# Output: username
```

### id
Show user ID and group IDs
```bash
# Show current user info
id

# Show specific user info
id username
```

### sudo
Execute command as superuser
```bash
# Run command as root
sudo command

# Switch to root shell
sudo -i

# Run command as another user
sudo -u username command

# Edit file with sudo
sudo nano /etc/hosts
```

### su (Switch User)
Switch to another user account
```bash
# Switch to root
su

# Switch to specific user
su username

# Switch with environment
su - username
```

### passwd
Change user password
```bash
# Change your password
passwd

# Change another user's password (requires sudo)
sudo passwd username
```

---

## Package Management (Debian/Ubuntu)

### apt / apt-get
Package manager
```bash
# Update package list
sudo apt update

# Upgrade installed packages
sudo apt upgrade

# Install package
sudo apt install package_name

# Remove package
sudo apt remove package_name

# Remove package and config files
sudo apt purge package_name

# Search for package
apt search keyword

# Show package info
apt show package_name

# Clean up
sudo apt autoremove    # Remove unused packages
sudo apt clean         # Clear package cache
```

---

## Process Management

### kill
Terminate processes
```bash
# Kill process by PID
kill 1234

# Force kill
kill -9 1234

# Kill by name
killall process_name

# Kill all processes by user
sudo killall -u username
```

### bg / fg
Background and foreground processes
```bash
# Run command in background (add & at end)
command &

# List background jobs
jobs

# Bring job to foreground
fg %1

# Send job to background
bg %1

# Suspend current process (Ctrl+Z)
# Then use bg to continue in background
```

---

## File Links

### ln (Link)
Create links to files
```bash
# Create hard link
ln source.txt link.txt

# Create symbolic (soft) link
ln -s /path/to/source.txt link.txt

# Create symbolic link to directory
ln -s /path/to/folder/ link_folder

# Remove symbolic link
rm link.txt    # Doesn't affect original file
```

**Hard Link vs Symbolic Link:**
- **Hard link:** Direct reference to file data (same inode)
- **Symbolic link:** Pointer to filename (like shortcut)

---

## Redirection & Pipes

### Output Redirection
```bash
# Redirect output to file (overwrite)
command > output.txt

# Redirect output to file (append)
command >> output.txt

# Redirect errors to file
command 2> error.txt

# Redirect both output and errors
command > output.txt 2>&1
command &> output.txt    # Shorter syntax

# Discard output
command > /dev/null
```

### Input Redirection
```bash
# Take input from file
command < input.txt

# Here document
cat << EOF
Line 1
Line 2
EOF
```

### Pipes (|)
Chain commands together
```bash
# Send output of one command to another
ls -l | grep ".txt"

# Multiple pipes
cat file.txt | grep "error" | wc -l

# Sort and display
ls | sort | less

# Count files
ls | wc -l
```

---

## Useful Shortcuts & Tips

### Command Line Shortcuts
```bash
# Ctrl+C = Cancel current command
# Ctrl+D = Logout / Exit
# Ctrl+Z = Suspend current process
# Ctrl+L = Clear screen (same as clear)
# Ctrl+A = Move to beginning of line
# Ctrl+E = Move to end of line
# Ctrl+U = Delete from cursor to beginning
# Ctrl+K = Delete from cursor to end
# Ctrl+R = Search command history
# Tab = Auto-complete
# !! = Repeat last command
# !$ = Last argument of previous command
```

### Wildcards
```bash
# * = Any characters
ls *.txt              # All .txt files
rm file*              # All files starting with "file"

# ? = Single character
ls file?.txt          # file1.txt, file2.txt, etc.

# [] = Character range
ls file[1-3].txt      # file1.txt, file2.txt, file3.txt
ls [abc]*.txt         # Files starting with a, b, or c

# {} = Multiple patterns
cp file.{txt,pdf} /backup/    # Copy both .txt and .pdf
```

### Command History
```bash
# Show command history
history

# Run command from history (number from history list)
!123

# Run last command
!!

# Run last command with sudo
sudo !!

# Search history (Ctrl+R)
# Then type to search, Enter to execute
```

---

## Quick Reference

### Most Essential Commands
```bash
ls          # List files
cd          # Change directory
pwd         # Current directory
mkdir       # Create directory
rm          # Delete
cp          # Copy
mv          # Move/rename
cat         # View file
nano        # Edit file
chmod       # Change permissions
sudo        # Run as admin
```

### Getting Help
```bash
# Show command manual
man command_name
man ls

# Show brief help
command_name --help
ls --help

# Search manual pages
man -k keyword


```
---

## User Account Management

### useradd (Add User)

Create new user accounts

```bash
# Create new user
sudo useradd username

# Create user with home directory
sudo useradd -m username

# Create user with specific shell
sudo useradd -m -s /bin/bash username

# Create user with specific UID
sudo useradd -u 1500 username

# Create user with expiry date
sudo useradd -e 2024-12-31 username

# Create user and add to groups
sudo useradd -m -G sudo,developers username
```

### adduser (Interactive User Creation)

```bash
# Create user interactively
sudo adduser username
```

### userdel (Delete User)

```bash
# Delete user (keeps home directory)
sudo userdel username

# Delete user and home directory
sudo userdel -r username

# Force delete even if logged in
sudo userdel -f username
```

### usermod (Modify User)

```bash
# Change username
sudo usermod -l newname oldname

# Change home directory
sudo usermod -d /home/newhome -m username

# Change shell
sudo usermod -s /bin/zsh username

# Add user to group
sudo usermod -aG groupname username

# Lock user account
sudo usermod -L username

# Unlock user account
sudo usermod -U username
```

### passwd (Password Management)

```bash
# Change your password
passwd

# Change another user's password
sudo passwd username

# Force password change on next login
sudo passwd -e username

# Lock user account
sudo passwd -l username

# Unlock user account
sudo passwd -u username

# Show password status
sudo passwd -S username
```

### groupadd (Add Group)

```bash
# Create new group
sudo groupadd groupname

# Create group with specific GID
sudo groupadd -g 1500 groupname
```

### groupdel (Delete Group)

```bash
# Delete group
sudo groupdel groupname
```

### groupmod (Modify Group)

```bash
# Rename group
sudo groupmod -n newname oldname

# Change GID
sudo groupmod -g 1500 groupname
```

### gpasswd (Group Management)

```bash
# Add user to group
sudo gpasswd -a username groupname

# Remove user from group
sudo gpasswd -d username groupname
```

### groups

```bash
# Show your groups
groups

# Show another user's groups
groups username
```

### id

```bash
# Show your user info
id

# Show another user's info
id username

# Show only UID
id -u

# Show only GID
id -g
```

### who

```bash
# Show logged in users
who

# Show your terminal
who am i
```

### w

```bash
# Show logged in users and activity
w

# Show specific user
w username
```

### whoami

```bash
# Display current username
whoami
```

### last

```bash
# Show recent logins
last

# Show specific user's logins
last username

# Show last 10 logins
last -n 10
```

### chage (Password Aging)

```bash
# Show password aging info
sudo chage -l username

# Force password change on next login
sudo chage -d 0 username

# Set password expiry (90 days)
sudo chage -M 90 username

# Set minimum days between changes
sudo chage -m 7 username

# Set warning days before expiry
sudo chage -W 14 username

# Set account expiry date
sudo chage -E 2024-12-31 username
```

### su (Switch User)

```bash
# Switch to root
su

# Switch to specific user
su username

# Switch with user's environment
su - username

# Run command as another user
su - username -c "command"
```

### visudo

```bash
# Safely edit sudoers file
sudo visudo
```

---

## User Account Files

### /etc/passwd

```bash
# View all users
cat /etc/passwd

# View specific user
grep username /etc/passwd

# Format: username:x:UID:GID:comment:home:shell
```

### /etc/shadow

```bash
# View encrypted passwords (requires sudo)
sudo cat /etc/shadow

# View specific user
sudo grep username /etc/shadow
```

### /etc/group

```bash
# View all groups
cat /etc/group

# View specific group
grep groupname /etc/group
```

---

## Practical Examples

### Create Complete User

```bash
# Create user with home and shell
sudo useradd -m -s /bin/bash john

# Set password
sudo passwd john

# Add to sudo group
sudo usermod -aG sudo john

# Verify
id john
groups john
```

### Lock/Unlock User

```bash
# Lock account
sudo passwd -l username

# Unlock account
sudo passwd -u username
```

### Set Password Policy

```bash
# Password expires every 90 days
sudo chage -M 90 username

# Minimum 7 days between changes
sudo chage -m 7 username

# Warn 14 days before expiry
sudo chage -W 14 username
```

### List All Users

```bash
# All users
cut -d: -f1 /etc/passwd

# Only human users (UID >= 1000)
awk -F: '$3 >= 1000 && $3 < 65534' /etc/passwd
```

### List All Groups

```bash
# All groups
cut -d: -f1 /etc/group

# Groups a user belongs to
groups username
```

---

## Tips & Best Practices

**Security:**

- ✅ Use strong passwords (12+ characters)
- ✅ Enforce password expiry
- ✅ Use principle of least privilege
- ✅ Lock unused accounts
- ✅ Use `sudo` instead of root login

**Common Mistakes:**

- ❌ Don't share passwords
- ❌ Don't give unnecessary sudo access
- ❌ Don't forget to remove old accounts
- ❌ Don't modify /etc/passwd directly

---

*This cheat sheet covers essential Linux commands. For more details, use `man command_name` to read the full manual.*


