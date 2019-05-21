FROM nginx:latest

COPY index.html /var/www/
COPY img /var/www/img

EXPOSE 80

COPY nginx.conf /etc/nginx/nginx.conf

CMD ["nginx"]
