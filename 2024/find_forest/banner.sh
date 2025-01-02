#!/bin/bash

echo -e "\n#################################################"
echo -e   "#                                               #"
echo -e   "#   Sir Gopher received an inventory of tree    #"
echo -e   "#       hollows in neighboring countries.       #"
echo -e   "#   We should help him find a tree hollow in    #"
echo -e   "#                Finnish forest.                #"
echo -e   "#                                               #"
echo -e   "#        Sir Gopher knows three things:         #"
echo -e   "#        1) The file extension is '.fin'        #"
echo -e   "#    2) File was created exactly one year and   #"
echo -e   "#        one day before the current date        #"
echo -e   "#        3) There is also a word 'forest'       #"
echo -e   "#                in the filename                #"
echo -e   "#                                               #"
echo -e   "#################################################"


if [[ $(whoami) != "vsfi" ]]; then
    bash
fi
