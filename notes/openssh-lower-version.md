# openssh lower version

{% embed url="https://unix.stackexchange.com/questions/402746/ssh-unable-to-negotiate-no-matching-key-exchange-method-found" %}

just add this below in you ~/.ssh/config file with host as the target machine

```text
Host 10.10.10.7
    Ciphers 3des-cbc
    KexAlgorithms +diffie-hellman-group1-sha1
```

