# more shell

```text
openssl passwd -6 -salt xyz 1234
python3 -c 'import crypt; print(crypt.crypt("1234", "$6$1234"))'
python -c 'import crypt; print crypt.crypt("1234", "$6$1234")'
perl -e 'print crypt("password","\$6\$saltsalt\$") . "\n"'
```

