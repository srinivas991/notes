# smbserver.py

```
smbserver.py -u guest -password guest -smb2support kalishare $(pwd)
net use x: \\10.10.14.28\kalishare /user:guest guest
```

```
impacket-smbserver kalishare `pwd`
dir \\10.10.14.25\kalishare
```

mount smb share on Kali Linux, refer here if you want to do more with shares etc - [https://0xdf.gitlab.io/2019/09/07/htb-bastion.html](https://0xdf.gitlab.io/2019/09/07/htb-bastion.html)

```
mount -t cifs //10.10.10.134/backups /mnt -o user=,password=
```
