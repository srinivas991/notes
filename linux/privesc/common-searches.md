# common searches

SEARCH FOR A TEXT

```
find -type f -exec grep -iaH "PGP PRIVATE KEY" {} 2>/dev/null +
find -type f -print0 2>/dev/null | xargs -0 grep -iaH "PGP PRIVATE KEY"
```

TEXT TO CHECK FOR:

```
PGP PRIVATE KEY
OPENSSH PRIVATE
'password' =>
password=
```

to search for SHA1 hashes - can be used for all kind of hashes

```
grep -iaHER "[0-9a-f]{40}" /var/www/ => checks for hashes length >= 40
find -type f| grep -E '\.php$|\.config$|\.conf' | while read f; do grep -iaEH password $f && echo $j; done;
```

for potential passwords

```
find / -type f 2>/dev/null | grep htpasswd
```
