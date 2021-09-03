#!/bin/bash

box=$1

while true; do
  if [[ $(nslookup $box | grep "NXDOMAIN") ]]; then
    echo "Can't nslookup, exiting"
    exit 1
  fi
  sshuttle -r htb-srinivas37@$box 10.129.0.0/16
  sleep 2
done
