## du

About this command
**du** is a command in Linux (short for disk usage) which helps you identify what files/directories are consuming how much space. If you run a simple `du` command in terminal.

```bash
du -a ~/Kioptrix 
4       /home/kali/Kioptrix/allport.txt
4       /home/kali/Kioptrix/3.c
12      /home/kali/Kioptrix

```

| Flag        | Description                                                                                                           |
| ----------- | --------------------------------------------------------------------------------------------------------------------- |
| -a          | Will list files as well as the folders                                                                                |
| -h          | will list the file sizes in human readable format (B,KBs, MBs)                                                        |
| -c          | Using this flag will print the total size at the end. Jic you want to find the size of directory you were enumerating |
| -d <number> | Flag to specify the depth-ness of a directory you want to view the results for (eg. -d 2)                             |
| --time      | To get the results with time stamp of last modified.                                                                  |
**Example**

`du -a /home/` will list every file in the /home/ directory with their sizes in KB.

If there's a lot of output you can surely use grep...

`du -a /home/ | grep user` will list any file/directory whose name is containing the string "_user_" in it.

  

**Final Words**

du command can alternate `ls` with the following flags:

`du --time -d 1 .`

It won't specify you the user ownership though, so you can use `stat` command on the file you want to know who is the owner of that particular file 

Syntax: `stat`


---

## Grep, Egrep, Fgrep

**Introduction**
It is a must known tool to everyone and that's why linux modules won't be complete without doing a mention of its amazing charisma. This tool, is what filters the good output we need from the residue. The official documentation says, The grep filter searches a file for a particular pattern of characters, and displays all lines that contain that pattern. The pattern that is searched in the file is referred to as the regular expression. The pattern is what I am gonna brief you about.

Syntax: `grep "PATTERN" file.txt` will search the file.txt for the specified "PATTERN" string, if the string is found in the line, the grep will return the whole line containing the "PATTERN" string.

Important Flags

|       |                                                                                                                                                                                           |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Flags | Description                                                                                                                                                                               |
| -R    | Does a recursive grep search for the files inside the folders(if found in the specified path for pattern search; else grep won't traverse diretory for searching the pattern you specify) |
| -h    | If you're grepping recursively in a directory, this flag disables the prefixing of filenames in the results.                                                                              |
| -c    | This flag won't list you the pattern only list an integer value, that how many times the pattern was found in the file/folder.                                                            |
| -i    | I prefer to use this flag most of the time, this is what specifies grep to search for the PATTERN while IGNORING the case                                                                 |
| -l    | will only list the filename instead of pattern found in it.                                                                                                                               |
| -n    | It will list the lines with their line number in the file containing the pattern.                                                                                                         |
| -v    | This flag prints all the lines that are NOT containing the pattern                                                                                                                        |
| -E    | This flag we already read above... will consider the PATTERN as a regular expression to find the matching strings.                                                                        |
| -e    | The official documentation says, it can be used to specify multiple patterns and if any string matches with the pattern(s) it will list it.                                               |


---

## Did someone said STROPS

String Manipulations (STRing OPerationS)

Many people discard this topic in their tutorials/courses, which I believe is leaving behind the true power of linux and it's terminal interface. You ever see someone typing a very long command piping their outputs into some other commands? Well believe me when I say, you can select a single byte character from a GB long array of string bytes, if you could master that. 

If you're from a programming background you might have used indexing in arrays, slicing in python, or even grepping in terminal... All are a means of string manipulations. Especially in bash, we have a TON of tools to perform a same kind of operation, with different flags or string patterns specified, but obviously we will be choosing the one, providing us the shortest and easiest syntax possible. 

For strops, we have the following tools that I always keep in my arsenal and you should too:

- tr
- awk
- sed
- xargs

Other commands to be familiar with:

- sort
- uniq


**tr**
Translate command(`tr`) can help you in number of ways, ranging from changing character cases in a string to replacing characters in a string. It's awesome at it's usage. Plus, it's the easiest command and a must know module for quick operations on strings.

Syntax: `tr [flags] [source]/[find]/[select] [destination]/[replace]/[change]`

This I guess is an appropriate representation of how you can use this tool. Moreover, we have the following flags offered by this command:

|   |   |
|---|---|
|Flags|Description|
|-d|To delete a given set of characters|
|-t|To concat source set with destination set(destination set comes first; t stands for truncate)|
|-s|To replace the source set with the destination set(s stands for squeeze)|
|-c|This is the REVERSE card in this game, for eg. If you specify -c with -d to delete a set of characters then it will delete the rest of the characters leaving the source set which we specified (c stands for complement; as in doing reverse of something)|
```bash

cat file.txt | tr -s '[:lower:]' '[:upper:]'
```

**awk**

The AWK Command

This is the most-est powerful tool in my arsenal, I can't think of any other command that can do something and not awk. It's like the all-in-one tool. If you ever played CSGO, you can totally relate AWK with AWP.

  

_"Awk is a scripting language used for manipulating data and generating reports.The awk command programming language requires no compiling, and allows the user to use variables, numeric functions, string functions, and logical operators."_

Sidenote: Just because it's the super tool, that's not necessary that there is no need to learn about other tools. The awk commands can be fairly longer to solve an operation than that of sed or xargs. A GNU project of awk (namely, gawk) which is also the one installed on every linux distro, is compatible with both awk and nawk( New-awk; also project by AT&T).

Syntax: `awk [flags] [select pattern/find(sort)/commands] [input file]`

Note: awk does support getting output via piping.

- If the commands you wrote are in a script you can execute the script commands by using the `-f` flag and specifying the name of the script file. (`awk -f script.awk input.txt`)

Using AWK

- To simply print a file with awk.

```bash

awk -f script.awk input.txt #If the commands you wrote are in a script you can execute the script commands by using the -f flag and specifying the name of the script file. (awk -f script.awk input.txt)


cat file.txt

#same thing using awk
awk '{print}' file.txt

cat awk_1611727975315.txt                                                   
ippsec youtube hackthebox 34024
john youtube ctf 50024
thecybermentor tcmsec courses 25923
liveoverflow youtube ctf 45345
nahamsec hackerone bughunting 12365
stok hackerone bughunting 1234

#Download the above given file `awk.txt`, and use the `awk` command to print the following output: 
'''_ippsec:34024  
john:50024  
thecybermentor:25923  
liveoverflow:45345  
nahamsec:12365  
stok:1234_
'''

 awk 'BEGIN{OFS=":"} {print $1$4}' awk_1611727975315.txt                    
ippsec34024
john50024
thecybermentor25923
liveoverflow45345
nahamsec12365
stok1234


```
