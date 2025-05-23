FROM ubuntu:latest
LABEL maintainer="FT"

RUN apt update && apt install -y python3

COPY increment.sh /increment.sh
COPY affichage.py /affichage.py

RUN chmod 755 /increment.sh

ENTRYPOINT ["/increment.sh"]
