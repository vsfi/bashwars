FROM alpine
LABEL maintainer="SilvanD"

ARG username=vsfi

RUN apk add bash mandoc man-pages
RUN adduser --disabled-password ${username}
WORKDIR /home/${username}
COPY dump.txt /home/${username}/dump.txt

COPY banner.sh /bin/banner
RUN chmod +x /bin/banner

RUN rm /bin/ps /bin/cat /bin/ls /bin/echo /bin/sed /usr/bin/tr /usr/bin/awk /usr/bin/cut /usr/bin/head /usr/bin/tail

RUN echo "ps() { printf 'Pssst! Nothing here!\n'; }" >> /home/${username}/.bashrc
RUN echo "ls() { printf 'There is something somewhere, who knows...\n'; }" >> /home/${username}/.bashrc
RUN echo "cat() { printf 'Meow\n'; }" >> /home/${username}/.bashrc
RUN echo "sort() { printf 'Not this time\n'; }" >> /home/${username}/.bashrc
RUN echo "awk() { printf 'Well, yes, but no\n'; }" >> /home/${username}/.bashrc
RUN echo "cut() { printf 'Cut it!\n'; }" >> /home/${username}/.bashrc
RUN echo "uniq() { printf 'You are unique, but this utility is not\n'; }" >> /home/${username}/.bashrc
RUN echo "head() { printf 'Lost your head?\n'; }" >> /home/${username}/.bashrc
RUN echo "tail() { printf 'Admins have no tails\n'; }" >> /home/${username}/.bashrc
RUN echo "tr() { printf 'Translator needed, we are hiring\n'; }" >> /home/${username}/.bashrc
RUN echo "grep() { printf 'Grepped the emptiness\n';}" >> /home/${username}/.bashrc
RUN echo "sed() { printf 'This is not coreutils, but you do not have it, sry\n'; }" >> /home/${username}/.bashrc
RUN echo "echo() { printf 'Hello? hello... lo... o...\n'; }" >> /home/${username}/.bashrc

ENV ENV=/home/${username}/.bashrc

ENTRYPOINT ["/bin/banner"]
USER ${username}
