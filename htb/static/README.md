### STATIC (no progress)

from nmap scans, our only entry point is 8080 port, since the other two are ssh ports

```
8080/tcp open  http    Apache httpd 2.4.38 ((Debian))
| http-robots.txt: 2 disallowed entries 
|_/vpn/ /.ftp_uploads/
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

lets explore these two paths,

ffuf on 8080, 8080/.ftp_uploads, 8080/vpn

just robots and blank page on 8080, onto .ftp_uploads,

`wget http://static.htb:8080/.ftp_uploads/db.sql.gz` from ftp_uploads, (looks like a rabbit hole to me), lets go on to vpn, we can come back here later

ffuf on vpn,

`ffuf -u http://static.htb:8080/vpn/FUZZ -e .php,.txt -w /usr/share/dirb/wordlists/common.txt`

```
actions.php             [Status: 302, Size: 0, Words: 1, Lines: 1]
database.php            [Status: 200, Size: 0, Words: 1, Lines: 1]
header.php              [Status: 200, Size: 0, Words: 1, Lines: 1]
index.php               [Status: 302, Size: 0, Words: 1, Lines: 1]
index.php               [Status: 302, Size: 0, Words: 1, Lines: 1]
login.php               [Status: 200, Size: 358, Words: 14, Lines: 7]
panel.php               [Status: 302, Size: 0, Words: 1, Lines: 1]
src                     [Status: 301, Size: 312, Words: 20, Lines: 10]
```

we have a login page, but dont have any clue, 

i think some sort of proxying we need to do with the /vpn/src url,

```
GET /vpn/src HTTP/1.1
Host: static.htb:8080
----
HTTP/1.1 301 Moved Permanently
Date: Wed, 28 Jul 2021 16:51:30 GMT
Server: Apache/2.4.29 (Ubuntu)
Location: http://172.20.0.10/vpn/src/
```

not much clue on other pages actually, lets try something on login.php

not much on login.php, tried some sql injection type of stuff, doesn't seem to be anything, I dont want to brute usernames / passwords anything yet

we got an username admin `gunzip < db.sql.gz`