FROM alpine:3.12.0

# copy crontabs for root user
RUN apk add --no-cache curl
COPY root /etc/crontabs/root
COPY daily.sh /usr/local/bin/daily.sh
COPY ping.sh /usr/local/bin/ping.sh

# start crond with log level 8 in foreground, output to stderr
CMD ["crond", "-f", "-d", "8"]
