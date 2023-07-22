FROM alpine
LABEL maintainer="KirillRevaa"
ARG username=vsfi

RUN apk add mandoc man-pages coreutils-doc less less-doc jq
RUN adduser --disabled-password ${username}

WORKDIR /home/${username}

COPY data.json /home/${username}/data.json
COPY template.html /home/${username}/template.html
COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

ENTRYPOINT ["/bin/banner"]
USER ${username}
