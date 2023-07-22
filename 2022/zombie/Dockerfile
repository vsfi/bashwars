FROM alpine
LABEL maintainer="wrathinmind"

# RUN 
RUN apk add mandoc man-pages coreutils-doc less less-doc gcc musl-dev

WORKDIR /data
COPY child.c .
RUN gcc child.c -o child 
COPY *.sh .
COPY *.txt .
RUN chmod +x *.sh

ENTRYPOINT ["/data/runner.sh"]

CMD /data/runner.sh