FROM alpine
LABEL maintainer="KirillRevaa"
ARG username=vsfi

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc python3 grep-doc
RUN adduser --disabled-password ${username}
RUN ln -sf /proc/1/fd/1 /stdout.log 
WORKDIR /home/${username}

COPY banner.sh /bin/banner
COPY check.py /check
COPY mock.py /py_files/mock.py
RUN for fl in $(seq 1 10); do cp /py_files/mock.py /py_files/manager-"$(tr -dc a-z0-9 </dev/urandom | head -c 25 ; echo '')".py; done
RUN for fl in $(seq 1 10); do cp /py_files/mock.py /py_files/rabotyaga-"$(tr -dc a-z0-9 </dev/urandom | head -c 25 ; echo '')".py; done
RUN rm /py_files/mock.py
COPY run_process.sh /bin/run_process
RUN chmod +x /bin/run_process && chmod +x /bin/banner && chmod 400 /check

ENTRYPOINT ["/bin/banner"]
