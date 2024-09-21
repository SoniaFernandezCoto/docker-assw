FROM alpine:latest
RUN apk add --no-cache sqlite sqlite-dev
WORKDIR /var/lib/sqlite
COPY init.sql /init.sql
EXPOSE 8000
CMD ["sh", "-c", "sqlite3 app.db < /init.sql && tail -f /dev/null"]
