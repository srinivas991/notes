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

![](../../.gitbook/assets/image%20%286%29.png)

we can see that one of them is valid, and should be changed.

![](../../.gitbook/assets/image%20%288%29.png)

once we change it, we can do stuff.

based on rpcenumeration, using enumdomusers and queryusergroups, found that sthompson is a domain admin, and both sthompson and svc-print are part of IT\_Accounts

