#!/bin/sh
if [ "$USER" != "vsfi" ]; then
    FLASK_APP=/root/webapp.py flask run --host=0.0.0.0 1>/dev/null 2>&1 &
    echo "127.0.0.1 stats.vsfi.org" >> /etc/hosts
    nginx
fi
echo -e "\n###############################################################################"
echo -e   "#    Hi there, it's me, Garfield!                                             #"
echo -e   "#                                                                             #"
echo -e   "#    I have to get some stats from the our stats server.                      #"
echo -e   "#    It's pretty easy: just make GET request to stats.vsfi.org/dt=YYYYmmdd    #"
echo -e   "#    where's YYYYmmdd is a date, but as far as you know I hate Mondays :(     #"
echo -e   "#                                                                             #"
echo -e   "#    Could you please get Mondays' stats from today                           #"
echo -e   "#    till the end of the year for me?                                         #"
echo -e   "#                                                                             #"
echo -e   "#    Sincerely yours,                                                         #"
echo -e   "#    Garfield                                                                 #"
echo -e   "###############################################################################"

if [ "$USER" != "vsfi" ]; then
    su vsfi -c "sh"
fi