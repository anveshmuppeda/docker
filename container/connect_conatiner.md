# start a container
$ docker run --name nginx --rm -p 8080:80  -d nginx

# create and connect to a bash shell in the container
$ docker exec -it nginx bash

root@a84ad71521b1:/#
