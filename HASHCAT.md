### HASHCAT

(google for) hashcat exmaple hashes

have a basic list

#### List generation with hashcat rules

so, a rule basically modifies and appends to your list of passwords, based on what you specify in your rules

`hashcat --force --stdout pwlist.txt -r /usr/share/hashcat/rules/best64`


#### getting pass policy from a domain

`cme smb $IP --pass-pol -u '' -p ''`

or maybe use enum4linux