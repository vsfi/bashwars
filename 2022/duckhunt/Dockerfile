FROM alpine

LABEL maintainer="wrathinmind"

WORKDIR /data
COPY frames/*.frame frames/
COPY banner.txt .
COPY *.sh .
RUN chmod +x *.sh

RUN adduser -D hunter

WORKDIR /home/hunter

ENTRYPOINT ["/data/banner.sh"]

CMD /data/banner.sh
