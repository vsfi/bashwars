#!/bin/sh
exec 100>>/home/vsfi/answer.txt
su vsfi -c "rm -f /home/vsfi/answer.txt; banner"