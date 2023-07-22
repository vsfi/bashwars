FROM alpine

LABEL maintainer="k-pf"
LABEL desc="curl-curl task"

ARG username=pahom

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc jq curl python3

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install flask

RUN rm /usr/bin/wget
RUN touch /usr/bin/wget
RUN chmod 700 /root
RUN chmod 700 /usr/bin/python3

COPY main.py /root/
RUN adduser --disabled-password ${username} 

WORKDIR /tmp

ENTRYPOINT ["/bin/banner"]