FROM golang:alpine as generator
COPY main.go .
RUN go build main.go

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
    iproute2 \
    net-tools \
    lsof \
    bc \
    man && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -yqq clean
RUN adduser --gecos "" --disabled-password ${username}
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /home/${username}
COPY --from=generator /go/main /var/main
COPY equation.txt /home/${username}/equation.txt
COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

USER ${username}
RUN echo /bin/banner >> /home/${username}/.bashrc
ENTRYPOINT ["/bin/bash"]
