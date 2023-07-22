FROM alpine
ARG username=vsfi
LABEL maintainer="Saymeis"
RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc xz
RUN adduser --disabled-password ${username}

WORKDIR /home/${username}

COPY banner.sh /bin/banner

COPY task_folder /home/${username}/task
# readonly
RUN chown -R root:root /home/${username}

ENTRYPOINT ["/bin/banner"]
USER ${username}
