FROM alpine
LABEL maintainer="KirillRevaa"
RUN apk add --no-cache jq jq-doc mandoc man-pages coreutils-doc less less-doc
RUN adduser --disabled-password perdobus
COPY banner.sh /bin/banner.sh
RUN chmod +x /bin/banner.sh

USER perdobus
COPY files/efGZ8cyJ6tTrHL3Q.json /home/perdobus/1.json
COPY files/hBfhX9qh6qMzVR3K.html /var/log/hBfhX9qh6qMzVR3K.html
COPY files/WprNBdMZ9uw5zU9b.csv /etc/ssl/WprNBdMZ9uw5zU9b.csv
COPY files/gegdLqKHa9xp7NwB.xml /lib/apk/db/gegdLqKHa9xp7NwB.xml
WORKDIR /home/perdobus
ENTRYPOINT ["/bin/banner.sh"]