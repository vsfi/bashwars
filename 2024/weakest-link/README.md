# Weakest link

In general it is a task about just one thing: `curl -w`

## Answer

`b000bb00b135b00b135b00b135b00b135b00b135`

## Writeup

`cat urls | xargs -I {} curl -Ss --write-out ' %{time_total}\n' {} | sort -nr -k2 | head -n1 | awk '{print $1}'`
