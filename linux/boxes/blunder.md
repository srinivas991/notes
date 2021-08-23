# blunder

NMAP:

```text
PORT   STATE  SERVICE VERSION
21/tcp closed ftp
80/tcp open   http    Apache httpd 2.4.41 ((Ubuntu))
|_http-generator: Blunder
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Blunder | A blunder of interesting facts
```

this box is a bit weird in its configuration, when I've tried to open the /admin page that we've go from fuzzing, it redirects to another IP, which is the box's IP like, 10.10.10.191 \(even when the box is a private machine which has some IP like 10.129.219.2, So, i've had to spin this up in a VIP VPN

 from some fuzzing, we get some files, which are, todo.txt, robots.txt, admin, install.php. These four gives us a lot of information

```text
/install.php => Bludit is already installed ;)
/todo.txt => -Inform fergus that the new blog needs images - PENDING
/admin => confirms the application runnign here - bludit
```

so, this confirms us that we have something called bludit here, when we search for exploits for this

![](../../.gitbook/assets/screenshot-2021-08-23-at-22.46.31.png)

but we dont know the version yet, lets try to find out by browing the github page of bludit. I've browsed a bit in the bludit github, to find this which reveals the version, if that file exists in the app root

{% embed url="https://github.com/bludit/bludit/blob/master/bl-plugins/version/metadata.json" %}

so, when we browse to that URL above from our app i.e /bl-plugins/version/metadata.json, we get the version. so, from the searchsploit results, we find that it has bunch of exploits, and all of them are authenticated exploits. if you remember, we've got a file before, todo.txt, which revealed us a username called fergus

so, after some fuzzing, there isn't much other than this bludit which we can really exploit, so we need to find a password for the fergus user to try and login into the admin page. So, lets use cewl for this now

`searchsploit -m php/webapps/48942.py` to get the exploit to the local machine. and now we can run this with the wordlist we generated with cewl `cewl -d 7 -m 7 http://10.10.10.191/ -w pwd.list` and user as fergus to try our luck. \(I really didn't this this would work\)

![](../../.gitbook/assets/screenshot-2021-08-23-at-23.00.56.png)

