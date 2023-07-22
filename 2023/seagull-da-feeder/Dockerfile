FROM python:3 as stage
LABEL maintainer="k-pf"
COPY . /data/
WORKDIR /data
RUN python generator.py

FROM alpine

ARG username=vsfi

RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc nginx openssl ca-certificates grep-doc
RUN adduser --disabled-password ${username}

WORKDIR /home/${username}

COPY banner.sh /bin/banner
COPY entrypoint.sh /bin/entrypoint
RUN chmod +x /bin/banner /bin/entrypoint

COPY --from=stage /data/etc_hosts.txt /etc/hosts.aliases
COPY --from=stage /data/all_hosts.txt /home/${username}/my_web_sites.txt
COPY --from=stage /data/nginx.conf /etc/nginx/http.d/default.conf
COPY --from=stage /data/rootCA.crt /etc/ssl/certs/rootCA.crt
COPY --from=stage /data/*.vsfi.org.cert /etc/nginx/certs/
COPY --from=stage /data/*.vsfi.org.key /etc/nginx/certs/

RUN cat /etc/ssl/certs/rootCA.crt >> /etc/ssl/certs/ca-certificates.crt
RUN update-ca-certificates

ENTRYPOINT ["/bin/entrypoint"]