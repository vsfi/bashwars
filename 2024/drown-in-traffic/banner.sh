#!/bin/bash

echo -e "\n##########################################################"
echo -e   "#                                                        #"
echo -e   "#   Sir Gopher dumped traffic from his assistant's PC.   #"
echo -e   "#      There is a suspicion that young worker also       #"
echo -e   "#      has a side job alongside with the main one.       #"
echo -e   "#                                                        #"
echo -e   "#        Find the most visited destination address       #"
echo -e   "#               in a dump file traffic.pcap              #"
echo -e   "#                                                        #"
echo -e   "#         Look only fot IPV4 addresses and ignore        #"
echo -e   "#             addresses from private network.            #"
echo -e   "#                                                        #"
echo -e   "##########################################################"
if [[ $(whoami) != "vsfi" ]]; then
    bash
fi