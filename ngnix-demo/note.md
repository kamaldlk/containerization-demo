
### pull image and run in docker
    docker pull nginx
    docker run --name nginx  -p 80:80 nginx
    docker rm nginx


### build our image and run
    docker build -t containerization-demo/nginx .
    docker run --name nginx  -p 80:80 containerization-demo/nginx
    docker rm nginx

###  CMD Vs ENTRYPOINT
    docker build -f Dockerfile-cmd -t containerization-demo/cmd-vs-entrypoint .
    docker run -it containerization-demo/cmd-vs-entrypoint
    docker run -it containerization-demo/cmd-vs-entrypoint < Name >