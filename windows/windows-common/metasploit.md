# Metasploit

Pivoting with metasploit

```text
# proxychains on 1080
# whatever we run with proxychains, will be routed through this proxy
socks4 127.0.0.1 1080

# on msfconsole, run the socks module which will start a listener on the local port
once we do that, add a route to the target server

lets say we have a meterpreter session with machine1, and the session is 3,
we need to add a route that looks like
route add 10.10.10.14 3 (10.10.10.14 is the host we are pivoting to)

once we do that, we can do this in msf to do a sort of nmap scan and run exploits
use auxillary/scanner/portscan/tcp
```

portforwarding with msf

```text
 # on meterpreter, probably can use this for pivoting kind of stuff as well
 portfwd add -l 445 -p 445 -r 127.0.0.1
```

