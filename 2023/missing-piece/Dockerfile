FROM alpine
LABEL maintainer="SilvanD"

ARG username=vsfi

RUN apk add mandoc man-pages coreutils-doc less less-doc
RUN adduser --disabled-password ${username}
WORKDIR /home/${username}
COPY answer.txt .
RUN chmod 666 answer.txt

COPY banner.sh /bin/banner
COPY entrypoint.sh /bin/entrypoint
RUN chmod +x /bin/banner /bin/entrypoint

ENTRYPOINT ["/bin/entrypoint"]