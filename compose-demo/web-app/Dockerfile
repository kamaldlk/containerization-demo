FROM nginx:latest

RUN apt-get clean
RUN apt-get update -y --fix-missing
RUN apt-get install -y curl

COPY index.html /var/www/

EXPOSE 80

COPY nginx.conf /etc/nginx/nginx.conf

CMD ["nginx"]
