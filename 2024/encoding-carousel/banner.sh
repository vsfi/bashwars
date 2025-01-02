#!/bin/bash

echo -e "\n#################################################################"
echo -e   "#                                                               #"
echo -e   "#   There is a web server here, we know the only endpoint:      #"
echo -e   "#              http://carousel.vsfi.org/initial                 #"
echo -e   "#    It looks like the response encoding is broken and          #"
echo -e   "#    the real one is in Content-Encoding header. Decode it      #"
echo -e   "#  and use the result as a next API endpoint unless the string  #"
echo -e   "#   begins with 'bw2024' - that would mean it's the answer.     #"
echo -e   "#                                                               #"
echo -e   "#################################################################"
if [[ $(whoami) != "vsfi" ]]; then
    bash
fi
