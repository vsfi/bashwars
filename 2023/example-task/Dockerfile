FROM alpine
LABEL maintainer="k-pf"
ARG username=vsfi

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc
RUN adduser --disabled-password ${username}

WORKDIR /home/${username}

RUN cat /dev/urandom | tr -dc '[:alpha:]' | fold -w ${1:-20} | head -n 31336 > file
RUN echo "WoH00y0uVefoUNDit123" >> file
RUN cat /dev/urandom | tr -dc '[:alpha:]' | fold -w ${1:-20} | head -n 68663 >> file

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

ENTRYPOINT ["/bin/banner"]
USER ${username}