FROM debian:bookworm
ARG DEBIAN_FRONTEND=noninteractive

ARG username=vsfi
RUN apt-get -yqq update && \
    apt-get -yqq install --no-install-recommends \
        less \
        man  \
        man-db \
        mandoc && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -yqq clean
RUN adduser --gecos "" --disabled-password ${username}
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /home/${username}

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

COPY trashfile.txt /home/vsfi/trashfile.txt

RUN rm /usr/bin/awk \
    /usr/bin/cat \
    /usr/bin/csplit \
    /usr/bin/cut \
    /usr/bin/echo \
    /usr/bin/expand \
    /usr/bin/fmt \
    /usr/bin/grep \
    /usr/bin/head \
    /usr/bin/paste \
    /usr/bin/perl \
    /usr/bin/pr \
    /usr/bin/printf \
    /usr/bin/sed \
    /usr/bin/split \
    /usr/bin/tail \
    /usr/bin/tr \
    /usr/bin/unexpand \
    /usr/bin/xargs

USER ${username}
RUN echo /bin/banner >> /home/${username}/.bashrc
ENTRYPOINT ["/bin/bash"]
