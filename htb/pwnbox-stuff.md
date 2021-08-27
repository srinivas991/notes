### PWN CONF

#### .tmux.conf profile
```bash
set -g prefix C-e
bind C-e send prefix
unbind C-b
set-option -g history-limit 10000
```

#### user_init script
```bash
HOME='/home/htb-srinivas37'

cat > $HOME/.tmux.conf << EOF
set -g prefix C-e
bind C-e send prefix
unbind C-b
set-option -g history-limit 10000
EOF

mkdir -p $HOME/.ssh

cat > $HOME/.ssh/authorized_keys << EOF
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDftxdkpzMnmosvb5g/Ueg2mvq+r8PY4mS74OIrYBUFvcQ5y8elqJBNlcwacKRqcr+hWKGplL5q8h2iG4S5o3kwB1r5OpY2FqwRhfUla/PFuvTCbnCyODLvQhVwsf1F+trGTKTiAfBari5eHzsf/SihHxPGedPUYDRv+s9Jd1nVWMQIPLGzO4yYu9F/uYC+htAyilbTp0Zspm9yXh+Q9+2TrB+SKkJpkpM45WGVqKfoUKnbkIiRa1SKO5HHaefX4Ydj35F/2wv3UKRVDJ1C7fQrdeOJBrjIB8L0Lqqx5xGmBV54AzrYzq/ecxaxY7WRB6ZmGnIo95OfbjHnOnirZkzu96DzkcLa2PpVmR40Wwq8WxqkK7438mUGkTo31dgaVaTzKsMfOymYTUS0kqJS/7qRfCBUaAoQ/3XHpPJYOJ888GT3m6jAPdyEkap+spLVsgdZ+xTNVVe/oAaQZYWv2wPNerIHsqr9EG0OqmsJzBxwPdaKqyb1j5g5Gajy/Olhw4k=
EOF

echo "AuthorizedKeysFile .ssh/authorized_keys" >> /etc/ssh/sshd_config
sudo systemctl restart ssh
```

#### common lists
```bash
common.txt:100
directory-list-2.3-medium.txt:100
raft-medium-words.txt:100
raft-large-words.txt:100
directory-list-lowercase-2.3-medium.txt:100
raft-medium-words-lowercase.txt:100
raft-medium-directories-lowercase.txt:100
```

#### enum.py
```python
#!/usr/bin/python3

import signal
import sys
import os

num_args = len(sys.argv)

sub_domain = sys.argv[1]
# run ffuf on subdomain

extensions = ''
if num_args > 2:
    extensions = sys.argv[2]

wl_prefix='/opt/useful/SecLists/Discovery/Web-Content'

print('Host: {}'.format(sub_domain))
print('Extensions: {}'.format(extensions))

os.system('mkdir fuzz_dir')

wl_location = "/home/htb-srinivas37/my_data/wordlists"

with open(wl_location, 'r') as wl:
    for j in wl.readlines():
        arr = j.strip().split(':')
        threads = arr[1] if len(arr) > 1 else 40
        if extensions == '':
            code = os.system('ffuf -ic -s -w {} -u http://{}/FUZZ -t {} >> fuzz_dir/{}'.format(wl_prefix + '/' + arr[0], sub_domain, threads, arr[0]))
        else:
            code = os.system('ffuf -ic -s -w {} -u http://{}/FUZZ -t {} -e {} >> fuzz_dir/{}'.format(wl_prefix + '/' + arr[0], sub_domain, threads, extensions, arr[0]))

        if code == signal.SIGINT:
            print('Done')
            sys.exit(0)
```

#### SSHUTTLE

```bash
sshuttle -r htb-srinivas37@htb-3swwzlqeir.htb-cloud.com 10.129.0.0/16
```
