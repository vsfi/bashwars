FROM debian:bookworm
LABEL maintainer="k-pf"
ARG DEBIAN_FRONTEND=noninteractive

ARG username=vsfi
RUN apt-get -yqq update && \
    apt-get -yqq install --no-install-recommends \
        locales \
        mandoc \
        coreutils \
        less \
        man-db \
        jq \
        curl \
        man \
        python3 \
        python3-flask \
        python3-gunicorn \
        nginx && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -yqq clean
RUN adduser --gecos "" --disabled-password ${username}
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8


RUN chmod 700 /root && chmod 700 /usr/bin/python3
COPY webapp.py /root/
COPY wsgi.py /root/

WORKDIR /home/${username}

COPY nginx.conf /etc/nginx/sites-available/default
COPY banner.sh /bin/banner
RUN chmod +x /bin/banner
COPY text /home/${username}/.text

ENTRYPOINT ["/bin/banner"]