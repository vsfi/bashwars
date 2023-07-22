from python:3.10 as stage

LABEL maintainer="k-pf"

RUN pip install Pillow numpy piexif
COPY . /data/
WORKDIR /data
RUN mkdir -p images
RUN python generate.py


FROM alpine
RUN apk update
RUN apk add mandoc man-pages coreutils coreutils-doc less less-doc grep-doc exiftool
RUN mkdir -p /home/vsfi

COPY --from=stage /data/images/ /home/vsfi
ADD banner.sh /bin/banner
RUN chmod +x /bin/banner

ENTRYPOINT ["/bin/banner"]
WORKDIR /home/vsfi
