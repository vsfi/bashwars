# Oh-yo-Cringe!

## Answer

`Yo won! How do Yo do, fellow kids?`

## Writeup

Get json, replace keys, post json, that's it

### sed

`curl -Ss -H "Content-type: application/json" --data "$(curl -Ss fellow.vsfi.org | sed 's/data/yo-data/g' | sed 's/tik-tok/yo-tik-tok/g' | sed 's/bts/yo-bts/g')" fellow.vsfi.org`

### jq

Take care of `-` in key  
`curl -Ss -H "Content-type: application/json" --data "$(curl -Ss fellow.vsfi.org | jq '. + {"yo-data": .data, "yo-tik-tok": ."tik-tok", "yo-bts": .bts} | del(.data, ."tik-tok", .bts)')" fellow.vsfi.org`
