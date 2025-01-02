FROM debian:bookworm
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
        nginx \
        python3 \
        python3-flask \
        python3-gunicorn && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -yqq clean
RUN adduser --gecos "" --disabled-password ${username}
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

COPY entrypoint.sh /bin/entrypoint
COPY webapp.py /opt/bashwars/webapp.py
COPY wsgi.py /opt/bashwars/wsgi.py
COPY nginx.conf /etc/nginx/sites-available/default
RUN chown -R root:root /opt/bashwars/ && chmod -R 700 /opt/bashwars/ && chmod 700 /bin/entrypoint

WORKDIR /home/${username}

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

RUN echo /bin/banner >> /home/${username}/.bashrc
ENTRYPOINT ["/bin/entrypoint"]
