FROM alpine
LABEL maintainer="KirillRevaa"

ARG username=vsfi

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc
RUN adduser --disabled-password ${username}

WORKDIR /home/${username}

COPY name_list /home/${username}/name_list
COPY stoplist /home/${username}/stoplist
COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

ENTRYPOINT ["/bin/banner"]
USER ${username}
