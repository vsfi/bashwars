# Trash Cleaner

The task is to cleanup `trashfile.txt`: remove all the newline chars, replace underscores with spaces, remove all the chars `[0-9!"№;%:?*()]` but latin letters.
The problem is a few popular utilities (such as `sed`, `grep`, `cat`, `awk`) are not available :(

## Answer

`vsfi is more than just competition`

## Writeup

```
text=`echo -n $(<trashfile.txt)`; regex='(.*)[0-9!@#$%^&*() ](.*)'; while [[ $text =~ $regex ]]; do text=${BASH_REMATCH[1]}${BASH_REMATCH[2]}; done; text=`echo ${text,,}`; echo ${text//_/ }
```
