FROM httpd:2.4

RUN apt-get update && apt-get install -y nodejs

COPY . /usr/local/apache2/htdocs/

EXPOSE 8080
