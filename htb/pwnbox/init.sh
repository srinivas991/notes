#!/bin/bash

HOME='/home/htb-srinivas37'

cat > $HOME/.tmux.conf << EOF
set -g prefix C-e
bind C-e send prefix
unbind C-b
set-option -g history-limit 10000
EOF

cat > $HOME/.vimrc << EOF
set number
syntax on
colorscheme default
set expandtab shiftwidth=4 softtabstop=4
set backspace=indent,eol,start
EOF

mkdir -p $HOME/.ssh

cat > $HOME/.ssh/authorized_keys << EOF
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDRP4/N65y0ttZhRaHCjfvBUY9odBHMR5l36L8aeqrL+go3SvKPHta3eXAvKCSgO6JHB/7/Ktz7bcmMus70YkyyWd5dIsx+DzxVvX6TptejQDYs3nzFfHMZetmZPboUp1u7vWc/ED8F79GsmNnDuxsg09qfw0mFmhvVdgWbeUmCgNEKUlawK1Bw44sg4NJhrIlgg3kLN0meJEBCJOrqTY6QRm3NSS14wNDSYxzcwdsVocvh3BhYrOjo/jAmiXmrMy0FoAU0+dEAqYk2kJPcOtoSLcrdC5s3jTvGk+ertIZU08Ju6QtTIDJZapu9wFXAxsKfNVIdBILlTVkC5ZN65fCooEcs6bWOt/EdjoJx44W5PtHbJulRY+uzPyPROraaq/LI6e7yBAM80rLOw0D7/FUKe+NilsLtj4ZKlUkaevIR7FC0XogftSYrqwUd7/jlB+LmYUb9Zi6l6YOfy6QImIXhVVhC88NNdqHz4pFGYsqG/KeI2cA9Z5w7Ndl4eGxEL2E=
EOF

echo "AuthorizedKeysFile .ssh/authorized_keys" >> /etc/ssh/sshd_config
sudo systemctl restart ssh
