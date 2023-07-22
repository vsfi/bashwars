FROM alpine
LABEL maintainer="KirillRevaa"
ARG username=vsfi

RUN apk add mandoc man-pages coreutils-doc less less-doc
RUN adduser --disabled-password ${username}

WORKDIR /home/${username}

ADD eva-00.tar.gz /home/${username}/

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

ENTRYPOINT ["/bin/banner"]
USER ${username}
