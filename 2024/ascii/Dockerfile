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
    wget \
    binwalk \
    ca-certificates \
    man && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -yqq clean
RUN wget -q https://github.com/TheZoraiz/ascii-image-converter/releases/download/v1.13.1/ascii-image-converter_Linux_amd64_64bit.tar.gz
RUN adduser --gecos "" --disabled-password ${username}
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN tar -zxf ascii-image-converter_Linux_amd64_64bit.tar.gz
RUN cp ./ascii-image-converter_Linux_amd64_64bit/ascii-image-converter /usr/bin/
RUN rm -rf ./ascii-image-converter_Linux_amd64_64bit && rm ascii-image-converter_Linux_amd64_64bit.tar.gz

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

USER ${username}
WORKDIR /home/${username}
COPY image.png .
RUN echo /bin/banner >> /home/${username}/.bashrc
ENTRYPOINT ["/bin/bash"]