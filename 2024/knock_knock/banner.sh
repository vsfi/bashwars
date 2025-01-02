#!/bin/bash

echo -e "\n################################################"
echo -e   "#                                              #"
echo -e   "#  Sir Gopher escaped from the forest and      #"
echo -e   "#  hid behind 7 proxies.                       #"
echo -e   "#                                              #"
echo -e   "#  He said he would open if                    #"
echo -e   "#  you'll knock for three times                #"
echo -e   "#  to the right port of http://localhost       #"
echo -e   "#  and specify the header                      #"
echo -e   "#      X-My-Shisha-Header: Gopher              #"
echo -e   "#                                              #"
echo -e   "#  How to find the right port?                 #"
echo -e   "#  Just solve the equation from your homedir!  #"
echo -e   "#                                              #"
echo -e   "################################################"

nohup /var/main >/dev/null 2>&1 &

if [[ $(whoami) != "vsfi" ]]; then
    bash
fi
