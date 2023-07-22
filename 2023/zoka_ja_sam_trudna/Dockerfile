FROM python:3 as stage
LABEL maintainer="k-pf"
COPY . /data/
WORKDIR /data
RUN python generator.py

FROM alpine

ARG username=vsfi

RUN apk add mandoc man-pages coreutils-doc less less-doc
RUN adduser --disabled-password ${username}

WORKDIR /home/${username}

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

COPY --from=stage /data/files/ /home/${username}/files

ENTRYPOINT ["/bin/banner"]
USER ${username}