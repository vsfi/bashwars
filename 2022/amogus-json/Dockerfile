FROM alpine 

RUN apk add --no-cache jq jq-doc mandoc man-pages coreutils-doc && mkdir -p /home/vsfi

ADD jsons/* /home/vsfi
ADD banner.sh /bin/banner
RUN chmod +x /bin/banner
ENTRYPOINT ["/bin/banner"]

WORKDIR /home/vsfi

