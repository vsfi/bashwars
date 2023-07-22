FROM alpine

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

ADD ./task/ /home/
WORKDIR /home/

CMD ["/bin/banner"]
