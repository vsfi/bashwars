FROM alpine
LABEL maintainer="k-pf"
ARG username=vsfi

RUN apk add --update mandoc man-pages coreutils coreutils-doc less less-doc python3 curl curl-doc nginx && rm -rf /var/cache/apk/*
RUN python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools && \
    pip3 install flask

RUN chmod 700 /root && chmod 700 /usr/bin/python3
RUN adduser --disabled-password ${username}
COPY webapp.py /root/


WORKDIR /home/${username}

COPY nginx.conf /etc/nginx/http.d/default.conf
COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

ENTRYPOINT ["/bin/banner"]
