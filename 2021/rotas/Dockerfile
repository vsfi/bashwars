FROM alpine

ARG username=rotas

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc jq curl python3
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install flask

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

RUN rm /usr/bin/wget
RUN touch /usr/bin/wget
RUN chmod 700 /root
RUN chmod 700 /usr/bin/python3

COPY main.py /root/

RUN adduser --disabled-password ${username}
COPY json.json /home/${username}

WORKDIR /home/${username}

ENTRYPOINT ["/bin/banner"]