FROM busybox

ARG username=popit

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

WORKDIR /tmp

COPY file.txt /tmp/access.log

RUN chmod 666 /tmp/*
RUN adduser -D ${username} 

CMD /home/hello
ENTRYPOINT ["/bin/banner"]
USER ${username}