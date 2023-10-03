FROM alpine

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc gcc musl-dev
COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

RUN adduser --disabled-password blitz 

COPY test.sh /home/blitz
RUN chmod 700 /home/blitz/test.sh

COPY runner.c /home/blitz
RUN gcc /home/blitz/runner.c -o /home/blitz/runner

RUN chmod 755 /home/blitz/runner
RUN chmod +s /home/blitz/runner
RUN rm /home/blitz/runner.c


COPY *.txt /home/blitz/

WORKDIR /home/blitz

ENTRYPOINT ["/bin/banner"]
