FROM alpine
ARG username=vsfi
LABEL maintainer="hdhog"

RUN apk add --no-cache \
    ca-certificates \
    less \
    ncurses-terminfo-base \
    krb5-libs \
    libgcc \
    libintl \
    libstdc++ \
    tzdata \
    userspace-rcu \
    zlib \
    icu-libs \
    curl

RUN apk -X https://dl-cdn.alpinelinux.org/alpine/edge/main add --no-cache \
    lttng-ust

RUN curl -L https://github.com/PowerShell/PowerShell/releases/download/v7.3.4/powershell-7.3.4-linux-alpine-x64.tar.gz -o /tmp/powershell.tar.gz \
    && mkdir -p /opt/microsoft/powershell/7 \
    && tar zxf /tmp/powershell.tar.gz -C /opt/microsoft/powershell/7 \
    && chmod +x /opt/microsoft/powershell/7/pwsh \
    && ln -s /opt/microsoft/powershell/7/pwsh /usr/bin/pwsh

RUN adduser --disabled-password ${username} -s /usr/bin/pwsh

WORKDIR /home/${username}

COPY banner.ps1 /bin/banner.ps1
COPY vms_export.csv /home/${username}/vms_export.csv
RUN chmod +x /bin/banner.ps1

# cleanup
RUN rm /bin/busybox 
USER ${username}
ENTRYPOINT ["pwsh", "/bin/banner.ps1"]