#!/bin/bash

echo -e "\n##########################################################"
echo -e   "#                                                        #"
echo -e   "#   There is a lot of trash data in trashfile.txt, you   #"
echo -e   "#  should remove every line break in this file, replace  #"
echo -e   "#   every '_' with a space and also remove every other   #"
echo -e   "#                character except letters.               #"
echo -e   "#  The resulted text should be converted to lower case.  #"
echo -e   "#                                                        #"
echo -e   "# You don't have access to 'cat', 'grep', 'sed' and etc. #"
echo -e   "#                     Good luck!                         #"
echo -e   "#                                                        #"
echo -e   "##########################################################"
if [[ $(whoami) != "vsfi" ]]; then
    bash
fi