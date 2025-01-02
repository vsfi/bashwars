# Example task

Sir Gopher dumped traffic from his assistant's PC. There is a suspicion that young worker also has a side job alongside with the main one.
Find the most visited destination address in a dump file traffic.pcap
Look only fot IPV4 addresses and ignore addresses from private networks.

## Answer

178.248.233.160

## Writeup

`tcpdump -qns 0 -r traffic.pcap 2>/dev/null | awk '{print $5}' | grep -P '\d+\.\d+\.\d+\.\d+' | grep -v '192\.168\|^10\.\|^172' | cut -d'.' -f-4 | sort | uniq -c | sort -nr | head -n1 | awk '{print $2}'`
