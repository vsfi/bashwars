#!/bin/sh
if [ "$USER" != "rotas" ]; then
    FLASK_APP=/root/main.py flask run --host=0.0.0.0 1>/dev/null 2>&1 &
fi
echo -e "\n######################################################"
echo -e   "#                                                    #"
echo -e   "#  Somewhere in json there's a node named 'yoururl'  #"
echo -e   "#  and there's an URL next to it                     #"
echo -e   "#                                                    #"
echo -e   "#  Are you able to get a flag from the URL?          #"
echo -e   "#                                                    #"
echo -e   "######################################################"

if [ "$USER" != "rotas" ]; then
    su rotas -c "sh"
fi