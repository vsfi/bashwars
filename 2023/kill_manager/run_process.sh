#!/bin/sh
for f in /py_files/*.py 
do 
    nohup python3 $f >/dev/null 2>&1 &
done