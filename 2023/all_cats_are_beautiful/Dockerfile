FROM alpine
LABEL maintainer="k-pf"
ARG username=vsfi
ARG filename="-Hi dear, do\n't you wanna read me?"

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc
RUN adduser --disabled-password ${username}

WORKDIR /home/${username}

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner
COPY answer.txt /home/${username}/${filename}
RUN echo 'not this file' > /home/${username}/.file_but_the_wrong_one
RUN echo 'not this file' > /home/${username}/not_this_one

ENTRYPOINT ["/bin/banner"]
USER ${username}