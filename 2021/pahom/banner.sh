#!/bin/sh
if [ "$USER" != "pahom" ]; then
    FLASK_APP=/root/main.py flask run --host=0.0.0.0 1>/dev/null 2>&1 &
fi
echo -e "\n##########################################################################"
echo -e   "# If you wanna be a browser you should acting like a browser:            #"
echo -e   "# follow redirects, read and write cookies, do not expose your weird UA. #"
echo -e   "# But you don't have a browser, just curl.                               #"
echo -e   "# If you'll be a good boy — http://localhost:5000 would return json with #"
echo -e   "# 'nextUrl' node which returns the flag                                  #"
echo -e   "##########################################################################"

if [ "$USER" != "pahom" ]; then
    su pahom -c "sh"
fi