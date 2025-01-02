#!/bin/bash

echo "127.0.0.1 carousel.vsfi.org" >> /etc/hosts
(cd /opt/bashwars/ && python3 -m gunicorn --bind 0.0.0.0:5000 wsgi:app --daemon)
nginx
su vsfi