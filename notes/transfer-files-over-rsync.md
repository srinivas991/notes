# transfer files over rsync

```text
rsync -aHAXxv --numeric-ids --delete --progress -e "ssh -T -o Compression=no -x" htb-srinivas37@htb-u1epkh7noe.htb-cloud.com:/tmp/new new/
```

