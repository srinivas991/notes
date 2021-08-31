# common methodology

* if there is a web server
  * browse through to see if there is a domain name in the js sources / etc in the view-source
  * 
* when ever you see a username, add it into the users file, same for any sort of passwords, even if its from any services or anything, just save everything to files. This helps if there is SSH access and one of the password is enabled. It doesn't hurt to gather them into two files, and this makes it easy for us to run hydra at any point of time or when we are stuck and it might be an easy win.

```text
common wordlists

/opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
/opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
/opt/useful/SecLists/Discovery/Web-Content/raft-small-words.txt
/opt/useful/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt
/opt/useful/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-small.txt
/usr/share/dirb/wordlists/common.txt
```

