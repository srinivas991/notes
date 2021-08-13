# Privesc

enumerate all the services running on localhost / 127.0.0.1

check for directory permissions on binary folders i.e not just the binary file permissions when using sudo -l

find 2 -type f -perm /4000 2&gt;/dev/null

check for backups

check write access to PATH locations, like /usr/sbin, sometimes you might be lucky

