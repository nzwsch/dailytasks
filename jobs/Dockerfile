FROM alpine:3.12.0

# copy crontabs for root user
COPY root /etc/crontabs/root

# start crond with log level 8 in foreground, output to stderr
CMD ["crond", "-f", "-d", "8"]
