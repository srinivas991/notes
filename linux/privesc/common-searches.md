# common searches

to search for SHA1 hashes - can be used for all kind of hashes

```text
grep -iIER "[0-9a-f]{40}" /var/www/ => checks for hashes length >= 40
find -type f| grep -E '\.php$|\.config$|\.conf' | while read f; do grep -iIEH password $f && echo $j; done;
```

for potential passwords

```text
find / -type f 2>/dev/null | grep htpasswd
```

