#!/bin/sh
python3 /home/vsfi/stream.py &
echo "127.0.0.1 signal.vsfi.org" >> /etc/hosts
su vsfi -c "banner"