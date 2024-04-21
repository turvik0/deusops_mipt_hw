FROM alpine:3.19 as builder
WORKDIR /app
RUN apk update && \
    apk add --no-cache curl nodejs npm && \
    rm -rf /var/cache/apk/*
COPY . .
ENV NPM_CONFIG_CACHE=/app/.npm-cache
RUN mkdir -p /app/.npm-cache && \
    chown -R 1001:1001 /app
RUN npm install
RUN npm run build

FROM alpine:3.19

RUN apk add --no-cache nginx

COPY --from=builder /app/build /var/www

RUN mkdir -p /run/nginx && \
    chown -R 1001:1001 /var/lib/nginx /var/log/nginx /run/nginx && \
    rm -rf /var/cache/apk/*

USER 1001

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]