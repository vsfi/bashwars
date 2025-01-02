# knock_knock_gopher

The task is to solve equation from the file to get server's port and knock in it three times using custom header.

## Answer

`You've found Sir Gopher!`

## Writeup

- `PORT=$(cat equation.txt | bc); seq 1 3 | xargs -I {} curl -Ss -H "X-My-Shisha-Header: Gopher" localhost:$PORT | tail -n1`
- `for i in $(seq 1 3); do curl -s --header "X-My-Shisha-Header: Gopher" http://localhost:$(cat equation.txt | bc)/ ; done | tail -n1`
