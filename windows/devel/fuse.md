# FUSE

nmap scan: domain controller along with port 80

![nmap](../../.gitbook/assets/image%20%285%29.png)

`DOMAIN: fabricorp.local`

not much I can get from the website, other than some user names, Couldn't find any other way that I can proceed forward. So looking at ippsec's wakthrough, we can generate a password list to try and bruteforce some of these passwords .so once we generate passwords using hashcat

`hashcat --force basic --rules /usr/share/hashcat/rules/best64.rule --stdout > mainlist1`

where my main list has stuff like this, and hashcat generate some 350 odd passwords

```text
fabricorp
fabricorp!
1fabricorp
Fabricorp
```

now, if we do,

`crackmapexec smb 10.10.10.193 -u users -p mainlist1`

![](../../.gitbook/assets/image%20%288%29.png)

we can see that one of them is valid, and should be changed.

![](../../.gitbook/assets/image%20%2820%29.png)

once we change it, we can do stuff.

based on rpcenumeration, using enumdomusers and queryusergroups, found that sthompson is a domain admin, and both sthompson and svc-print are part of IT\_Accounts

so, after some rcp enumeration and finding users and groups, if we check for printers, using enumprinters, we see a password in that output, which is the password for svc-print user - `$fab@s3Rv1ce$1`

![](../../.gitbook/assets/image%20%2818%29.png)

![](../../.gitbook/assets/image%20%287%29%20%281%29.png)

so my goto is to run bloodhound-python when ever we get a credentials, and if we ingest the data into bloodhound we find out that svc-print user can `PSRemote` into the box

![](../../.gitbook/assets/image%20%2825%29.png)

we run the pre-built query in bloodhound after marking user as owned - `Shortest Path from Owned Principals`

![](../../.gitbook/assets/image%20%2819%29.png)

so, lets `evil-winrm` into the box, and the first thing I check here is `whoami /priv`. which can be an easy win if you're trying to escalate privileges

![](../../.gitbook/assets/image%20%286%29.png)



