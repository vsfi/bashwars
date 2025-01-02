#!/bin/bash
if [[ $(whoami) != "vsfi" ]]; then
    echo "127.0.0.1 fellow.vsfi.org" >> /etc/hosts
    (cd /root/ && python3 -m gunicorn --bind 0.0.0.0:5000 wsgi:app --daemon)
    nginx
fi
echo -e "\n######################################################################################################"
echo -e   "#                              Yo yo! Snowboarding, diskette!                                        #"
echo -e   "#                                                                                                    #"
echo -e   "#    Gopher's father decided to be more cool and got IT lessons too.                                 #"
echo -e   "#    They've learned some basics, so, he's made a web-server fellow.vsfi.org and said:               #"
echo -e   "#    \"ma boy, if yo can add yo- for each of top-level keys and post it back — I'll give you a hug\"   #"
echo -e   "#                                                                                                    #"
echo -e   "#    Could you get a hug?                                                                            #"
echo -e   "#                                                                                                    #"
echo -e   "######################################################################################################"

if [[ $(whoami) != "vsfi" ]]; then
    su vsfi
fi
