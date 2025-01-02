# Phonetic alphabet

The main plot of this task is using `xargs`, `curl` and some cookie parsing

## Answer

`foxtrot_uniform_charlie_kilo`

## Writeup

There's a 'hidden' lyrics file in the home dir. The text in it looks like a set of URLs but the server responses don't contain response body. The thing is to collect the data from response cookies.

```
cat .text | xargs -I % curl -Ss -c - lyrics.vsfi.org% | grep "lyrics" | awk '{print $7}' | tr -d '\n'; echo
```
