FROM nginx:latest
LABEL maintainer="FT"

RUN apt update && apt install -y nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/

VOLUME ["/var/www/html"]

ENTRYPOINT ["nginx", "-g", "daemon off;"]
