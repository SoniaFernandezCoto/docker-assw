FROM httpd:2.4
# Instalar curl
RUN apt-get update && apt-get install -y curl && apt-get clean
COPY ./index.html /usr/local/apache2/htdocs/
