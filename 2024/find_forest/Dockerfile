FROM golang:alpine as generator
COPY main.go /
RUN go run /main.go

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
    man && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -yqq clean
RUN adduser --gecos "" --disabled-password ${username}
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /home/${username}
COPY --from=generator --chown=${username}:${username} /inventory /home/${username}/inventory

COPY banner.sh /bin/banner.sh
RUN chmod +x /bin/banner.sh

USER ${username}
RUN echo /bin/banner.sh >> /home/${username}/.bashrc
ENTRYPOINT ["/bin/bash"]
