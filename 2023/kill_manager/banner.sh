#!/bin/sh
echo -e "\n####################################"
echo -e   "#                                  #"
echo -e   "#  Kill all *.py proccesses        #"
echo -e   "#  But don't kill rabotyaga ones!  #"
echo -e   "#                                  #"
echo -e   "####################################"
set -e
if [ "$USER" != "vsfi" ]; then
    nohup python3 /check >/dev/null 2>&1 &
    su vsfi -c "/bin/run_process; sh"
fi