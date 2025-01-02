# Find forest

## Answer

`NICE HOLLOW`

## Writeup

`cat $(find inventory -mtime +366 -a -mtime -399 -name "*.fin" | grep forest)`
