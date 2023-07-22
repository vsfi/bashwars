FROM alpine/git

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc
COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

WORKDIR /wars

RUN git clone https://github.com/Cyberbeing/xy-VSFilter /wars

ENTRYPOINT ["/bin/banner"]