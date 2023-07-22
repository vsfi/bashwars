from python:3.10 as stage
LABEL maintainer="wrathinmind"

WORKDIR /data

COPY . /data
RUN mkdir -p files
RUN python generate.py

FROM alpine

WORKDIR /home
RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc
COPY --from=stage /data/files .
COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

ENTRYPOINT ["/bin/banner"]

