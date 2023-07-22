FROM busybox

ARG username=elite

WORKDIR /tmp
COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

COPY files /tmp/files/
RUN chmod -R 744 /tmp/files
RUN chmod 755 /tmp/files

RUN adduser -D ${username}

USER ${username}
ENTRYPOINT ["/bin/banner"]