FROM golang:1.20 as stage
LABEL maintainer="wrathinmind"
WORKDIR /data
COPY main.go .
RUN go mod init flash
RUN CGO_ENABLED=0 go build -a -installsuffix cgo -o server

FROM alpine
RUN apk update && apk add gettext bash

ARG username=vsfi

RUN apk add mandoc man-pages coreutils-doc less less-doc
RUN adduser --disabled-password ${username}

WORKDIR /home/${username}

COPY banner.sh banner.sh
COPY --from=stage /data/server .
RUN chmod +x banner.sh


ENTRYPOINT ["/home/vsfi/banner.sh"]
USER ${username}
