# Pirate bay

The task is to find the user who's made a request from the same IP address which Miron used for the majority of requests

# Answer

`mr.Pirate`

# Writeup

The solve is to find Miron's requests, find the most used IP and then find the user who used the same IP address

`` cat shop.log | grep `cat shop.log | grep Miron | awk '{print $1}' | sort | uniq -c | sort -r | head -n 1 | awk '{print $2}'` | grep -v Miron | awk '{print $12}' ``
