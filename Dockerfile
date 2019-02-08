FROM httpd:2.4

RUN apt-get update && apt-get install -y nodejs

COPY . .

EXPOSE 8080
