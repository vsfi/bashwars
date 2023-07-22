FROM golang:alpine as base
LABEL maintainer="red_horse"
COPY crackme.go crackme.go
RUN CGO_ENABLE=0 go build crackme.go

FROM alpine
ARG username=vsfi

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc
RUN adduser --disabled-password ${username}

WORKDIR /home/${username}

COPY --from=base /go/crackme /home/${username}/

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

ENTRYPOINT ["/bin/banner"]
USER ${username}