#!/usr/bin/env sh
# dirty hack to overwrite /etc/hosts
cat /etc/hosts.aliases >> /etc/hosts
nginx

su vsfi -c "/bin/banner; sh"