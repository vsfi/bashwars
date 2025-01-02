#!/bin/bash
if [[ $(whoami) != "vsfi" ]]; then
    echo "127.0.0.1 lyrics.vsfi.org" >> /etc/hosts
    (cd /root/ && python3 -m gunicorn --bind 0.0.0.0:5000 wsgi:app --daemon)
    nginx
fi
echo -e "\n###################################################################"
echo -e   "#                                                                 #"
echo -e   "#    Somebody once told me the lyrics file should be              #"
echo -e   "#    Somewhere in my home dir                                     #"
echo -e   "#    I was looking for it hardly but found something ugly         #"
echo -e   "#    Who invented this stupid http://lyrics.vsfi.org              #"
echo -e   "#                                                                 #"
echo -e   "#    Well, the letters start comin' and they don't stop comin'    #"
echo -e   "#    Find the proper ones and I bet it'll be funny                #"
echo -e   "#    Doesn't make sense to parse just for fun                     #"
echo -e   "#    Join them in a string and the task will be done              #"
echo -e   "#                                                                 #"
echo -e   "###################################################################"

if [[ $(whoami) != "vsfi" ]]; then
    su vsfi
fi
