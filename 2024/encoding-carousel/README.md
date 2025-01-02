# Encoding carousel

`http://carousel.vsfi.org` is an web-server with entrypoint `GET /initial`, every response has different encoding.
The task is to go through endpoints using correct encodings (obtained on the previous step from header) while response does not start with `bw2024` which is the answer.

## Answer

`bw2024_nice_script_u_made`

## Writeup

Oneliner:

```
PATHPART="/initial"; while [[ ! "$PATHPART" =~ ^bw2024 ]]; do PATHPART=$(curl http://carousel.vsfi.org$PATHPART 2>/dev/null | iconv -c -f $(curl -sI http://carousel.vsfi.org$PATHPART | grep Content-Encoding | awk '{print $2}') -t UTF-8); done; echo $PATHPART;
```

More readable explanation:

```
PATHPART="/initial"
while [[ ! "$PATHPART" =~ ^bw2024 ]]
do
  ENCODING=$(curl -sI http://carousel.vsfi.org$PATHPART | grep Content-Encoding | awk '{print $2}')
  PATHPART=$(curl http://carousel.vsfi.org$PATHPART 2>/dev/null | iconv -c -f $ENCODING -t UTF-8)
done
echo $PATHPART
```
