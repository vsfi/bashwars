# Flash service writeup


## TL;DR 
#### Solution using awk:

`export port=31337; export secret=""; while true; do $(envsubst <<< 'exec 3<>/dev/tcp/127.0.0.1/$port; echo $secret>&3; cat <&3' | bash | tee /dev/tty | grep -o -e 'send .*' | awk '{str = sprintf("export port=%s\nexport secret=%s", $5, $2)} END {print str}'); done`

####  Solution using echo and sed:

`export port=31337; export secret=""; while true; do $(echo "exec 3<>/dev/tcp/127.0.0.1/$port; echo $secret>&3; cat <&3" | bash | tee /dev/tty | grep -o -e 'send .*' | sed -E 's/\w+\s(\w+)\s\w+\s\w+\s(\d+)/export secret=\1\nexport port=\2/'); done`


## Explanation: 
### First, we need to communicate with localhost:31337

For this purpose we will use **/dev/tcp** and setup the channel
```
exec 3<>/dev/tcp/127.0.0.1/31337;
echo hello >&3; 
cat <&3
```

Thus we get the following line: `We are out of time! Quickly send 0a7a7f44CeE1f84A4F3716D7f1bb7De4 to port 34866`

When we repeat the command, it sends us new secret and port - looks like they are completely random

But when we send this **secret** string to the server's **port** manually, we see the following:

```
exec 3<>/dev/tcp/127.0.0.1/34866;
echo 0a7a7f44CeE1f84A4F3716D7f1bb7De4 >&3; 
cat <&3
```
**You are 101123 ms late**

Looks like we need to act like Flash - it means to hurry up.

Let's try to extract these secret and port and compose a new command to be run immediately.

### Extracting the data using awk and regex

Let's craft a new command. I use **grep** to cut out a part of the string

```
... exec 3<>/dev/tcp/127.0.0.1/31337; echo hello >&3; cat <&3 | grep -o -e 'send .*' | awk '{str = sprintf("exec 3<>/dev/tcp/127.0.0.1/%s;echo %s >&3;cat <&3", $5, $2)} END {print str}'
> exec 3<>/dev/tcp/127.0.0.1/23656;echo 94f4C7eCdF27C2dB04e35D1b6c8AD457 >&3;cat <&3
```

Now, let's send it to bash:
```
exec 3<>/dev/tcp/127.0.0.1/31337; echo hello >&3; cat <&3 | grep -o -e 'send .*' | awk '{str = sprintf("exec 3<>/dev/tcp/127.0.0.1/%s;echo %s >&3;cat <&3", $5, $2)} END {print str}' | bash
> Great, you are just in time! Quickly send 8C2534a7a648a8075aC3F9Fad4AFbdea to port 14905
```


You can clearly see, that we get another pair of **secret** and **port**

Probably, we need to automate the solution


### Templates and environment variables
My solution is to create a template, that will be filled with new variables

#### Adding environment variables
```
export port=31337; 
export secret=""; 
```

#### creating a template
```
envsubst <<< 'exec 3<>/dev/tcp/127.0.0.1/$port; echo $secret>&3; cat <&3'
```
You can also use `echo "exec 3<>/dev/tcp/127.0.0.1/$port; echo $secret>&3; cat <&3"` instead of envsubst

Let's execute the template and get the output
```
export port=31337; 
export secret=""; 
envsubst <<< 'exec 3<>/dev/tcp/127.0.0.1/$port; echo $secret>&3; cat <&3' | bash
> We are out of time! Quickly send FD6d2B6cCf968F60Fa381b205a7FaabF to port 37015
```

Great, now let's change the awk command to create new exported variables:
```
export port=31337; 
export secret=""; 
envsubst <<< 'exec 3<>/dev/tcp/127.0.0.1/$port; echo $secret>&3; cat <&3' | bash | grep -o -e 'send .*'| awk '{str = sprintf("export port=%s\nexport secret=%s", $5, $2)} END {print str}';
> export port=40738
> export secret=6dd89859e77829C6aabdCdDBf66B6728
```

We don't see the original answer - it might be useful.
For this purpose let's add a **tee** command between **bash** and **grep**:
```
bash | tee /dev/tty | grep
```

But we can't simply send the result to bash - it will be executed in new environment and then fade away. 

Let's leave new variables in our environment using `$()`: 
```
export port=31337; 
export secret=""; 
$(envsubst <<< 'exec 3<>/dev/tcp/127.0.0.1/$port; echo $secret>&3; cat <&3' | bash | tee /dev/tty | grep -o -e 'send .*'| awk '{str = sprintf("export port=%s\nexport secret=%s", $5, $2)} END {print str}');
echo $secret $port
> 9a8bD0C89BcA5BEdD47Fa744B0FA8Ce7 63730
```


#### Loop the whole thing:

```
export port=31337; 
export secret=""; 
while true; do
    $(envsubst <<< 'exec 3<>/dev/tcp/127.0.0.1/$port; echo $secret>&3; cat <&3' | bash | tee /dev/tty | grep -o -e 'send .*'| awk '{str = sprintf("export port=%s\nexport secret=%s", $5, $2)} END {print str}');
done
```

We see 1024 lines and the finally the flag:
```
...
Great, you are just in time! Quickly send EB65BD2d9F8a74aEbFb6b25C3e5b3EBB to port 11668
You made it in time! A Fla⚡️H in the night❗
```

#### How to break the loop?
It is your homework for now
<!-- if you only could break on pgrep -->


