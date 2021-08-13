# bypass TLS restriction

sometimes, some websites have these restrictions that use a lower version of TLS.

```text
# to change it in firefox
https://support.mozilla.org/en-US/questions/1101896

# for changing from commandline, useful when you're doing ffuf or something,
# you can also export the env var
export OPENSSL_CONF=~/.openssl_allow_tls1.0.cnf
https://askubuntu.com/questions/1250787/when-i-try-to-curl-a-website-i-get-ssl-error
```



