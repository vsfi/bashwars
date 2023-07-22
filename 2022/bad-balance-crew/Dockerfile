FROM alpine

LABEL maintainer="k-pf"

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc jq jq-doc curl curl-doc python3
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install flask

RUN rm /usr/bin/wget
RUN touch /usr/bin/wget
RUN chmod 700 /root
RUN chmod 700 /usr/bin/python3

COPY webapp.py /root/
COPY data.json /root/
COPY banner.sh /bin/banner
RUN chmod +x /bin/banner
RUN adduser --disabled-password bbalance

WORKDIR /home/bbalance

ENTRYPOINT ["/bin/banner"]
