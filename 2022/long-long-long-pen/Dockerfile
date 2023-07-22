FROM alpine

LABEL maintainer="Saymeis"

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc
RUN adduser --disabled-password michele
COPY banner.sh /bin/banner
RUN chmod +x /bin/banner
WORKDIR /michele
COPY ./_start.sh .

RUN chmod +x _start.sh
RUN sh _start.sh
RUN rm _start.sh

ENTRYPOINT ["/bin/banner"]