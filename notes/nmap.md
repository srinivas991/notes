# nmap

```text
# usual commands
sudo nmap -sS -sV -sC -oN nmap/nmap $IP
sudo nmap -sS -sV -sC -p- -oN nmap/fullmap $IP

# just run the safe scripts
nmap --script safe

# both vuln and safe
nmap --script "vuln and safe"

# grep for categories on the nmap scripts
grep -r categories /usr/share/nmap/scripts/*.nse

# get all categories
grep -r categories /usr/share/nmap/scripts/*.nse | grep -oP '".*?"' | sort -u

# default scripts
grep -r categories /usr/share/nmap/scripts/*.nse | grep default
```

