FROM alpine
LABEL maintainer="SilvanD"

ARG username=vsfi

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc python3
RUN adduser --disabled-password ${username}
WORKDIR /home/${username}
COPY stream.py .
COPY answer.txt .

RUN chmod 400 answer.txt
RUN chmod 700 stream.py

COPY banner.sh /bin/banner
COPY entrypoint.sh /bin/entrypoint
RUN chmod +x /bin/banner /bin/entrypoint

ENTRYPOINT ["/bin/entrypoint"]