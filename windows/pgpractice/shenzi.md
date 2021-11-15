# shenzi

shenzi IP: 192.168.59.55

#### Initial enumeration

enumerated for a long time, on different subdirectories, different ports.. this is what I got

![](<../../.gitbook/assets/image (28).png>)

lets first add shenzi into our hosts file, so that we dont have to type the IP addess everytime

![](<../../.gitbook/assets/image (33).png>)

full port scan is kind of irrelevant at this point, other than that we found an smb share wtih a file called passwords.txt in it, which had a bunch of passwords

![](<../../.gitbook/assets/image (32).png>)

lets get this file, and see whats inside it, only including the part of interest in the file

![](<../../.gitbook/assets/image (31).png>)

lets make a note of this, it looks like atleast one box in OSCP will have a wordpress in it if not more...

after quite some enumeration (scans / ffuf) on different places, going through the chat in OffSec discord, read that it might be helpful that if you get a box name, worth trying the /boxname on any http / https it might have.

![](<../../.gitbook/assets/image (7).png>)

indeed it does have something useful here, a wordpress site, lets login using the creds from passwords.txt we found before

as usual, lets go to the plugin editor page on wordpress, which can give us RCE on the box..

lets update the 404.php on the active theme, and save

![](<../../.gitbook/assets/image (27).png>)

now, navigate to a page which will trigger the 404 in the theme, here we have

![](<../../.gitbook/assets/image (29).png>)

now, lets take this to Burp Suite to make easier on getting a reverse shell hopefully..

