FROM nginxinc/nginx-unprivileged:alpine
USER root
#volume for static pages
VOLUME /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
#clear cache after installing utilities
RUN apk update && \
    apk add --no-cache vim && \
    rm -rf /var/cache/apk/* &&\
    chmod -R 777 /usr/share/nginx/html
EXPOSE 8080
USER nginx