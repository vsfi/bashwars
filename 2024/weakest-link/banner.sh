#!/bin/bash
if [[ $(whoami) != "vsfi" ]]; then
    echo "127.0.0.1 weakest-link.vsfi.org" >> /etc/hosts
    (cd /root/ && python3 -m gunicorn --workers 5 --bind 0.0.0.0:5000 wsgi:app --daemon)
    nginx
fi
echo -e "\n############################################################"
echo -e   "#                                                          #"
echo -e   "#     Would you like to play a game?                       #"
echo -e   "#                                                          #"
echo -e   "#     We have some urls, but one of them is tooo slow.     #"
echo -e   "#                                                          #"
echo -e   "#     Who's been anything but Entertainment Tonight?       #"
echo -e   "#     Whose parachute sadly has failed to open?            #"
echo -e   "#     Whose brain is illegally parked?                     #"
echo -e   "#     Who is as useful as an ashtray on a motorbike?       #"
echo -e   "#     Whose pinkie and brain are both the same size?       #"
echo -e   "#     Who thinks Tik Tok is a breath mint?                 #"
echo -e   "#     Whose lightbulb is getting dimmer?                   #"
echo -e   "#                                                          #"
echo -e   "#     Gimme response!                                      #"
echo -e   "#                                                          #"
echo -e   "############################################################"

if [[ $(whoami) != "vsfi" ]]; then
    su vsfi
fi
