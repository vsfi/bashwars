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


COPY webapp.py /root/
COPY wsgi.py /root/
COPY urls.py /root/
COPY nginx.conf /etc/nginx/sites-available/default
RUN chmod -R 700 /root && chmod 700 /usr/bin/python3
# put all urls in user's home dir
RUN (cd /root/ && python3 -c "from urls import urls; print('\n'.join(['http://weakest-link.vsfi.org/' + url for url in urls]))" > /home/${username}/urls)

WORKDIR /home/${username}

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

ENTRYPOINT ["/bin/banner"]
