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
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDc+OVbP1AmNJBrdyqfz6gT4+TlZfZfNE2OiUjVLlYqjRuD/kLajSSKoI+MSl6xBko8BVBdoYPJ1QSwvfUVRn7jKvoZkE1Tp9vZn6n5UN9WEytAQ/476X3dqic3cE4jVKCy9pLiuLRgBZa8bJ17gvodb/pLprwJHZtpd30IgZyBRabFXERUVwy1Bi3Wa50V0RwqF7cMlz1nzYBqZF6y5aZYQl4dX7LcdWk8hJUdYNkJ6os6qXAc/+t2vjcwmlrUPrVRWQM9R7hf3AwLtItYGvtrdNy5BoOm2Im+wxKxJroLS1c2C6THNLOOzv1AYhT687JGOYpsgxO3Ie/cVVzhD4d/8d6zMDwkn2qXcg2JXEP+SyhVJXLr1/3X0ggNEoDoZJeDIeOYqNAFgWcNP028Kfa7AMVHitzgh/kjQXxWHNl+3WPoa3oRKbCWT+SxsPbYwt422CQZZFCJ7gWcWxHQI8il9VWaJyZta7YPNO8KtlT+fdc2nUKXJf/EMPwngM8W5b8=
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDDcSfZU7PT8Vrm8UkLZYoThyc3c5OI6joz11kUvITVAdQQnfYTyfS/f4CaUsZWbeG+auDqOXXCqKsiPJzcrnaVoq1VSG38GtLKpaOZ5uUeWCKOJppuDpg1ik9zADNnmSUqU086vjIrHaXUGrGWQoJmbmC2zbyw6i/j//E4DGbuxT6m3QzuJyDPp/i5n/7MfIvkN5Z4b0G53qBSzZxquFvktJOZOQB51q3fBrOPYDfUscjHnDsISgJSGIzFxz98heW95G20kZaKhLsvfGllVqPLnZvyq5FYANkn2fQ01cFY8NfW8YjGdJjOLTdHDHt3kj2EJUf6MtqDJnWTIWqDkDjWcAFRlWfoz4LoudmbO1dkkOfBnojLEsR2YR8/6PlKh448Fa/Z2PQum6YRDWyFh2s0knn72HX885Gh1GwaD2ciuubEvvvyJK/4XeC3wfq8R2c1LUU1o02Sg7MuxuAi6y83+j+ql//W4sJ7LxiY5VJwKJlRop0BePHIqhQBKlQFvwM=
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
