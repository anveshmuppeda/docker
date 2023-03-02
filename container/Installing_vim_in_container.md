Installing Vim in a Docker Container
#
docker
#
vim
I just realized that my docker container did not have vim installed, and had to google some commands.

All you need to do is run the commands below in the container. These commands are mainly used in Ubuntu containers.

#**apt-get update**

##**apt-get install vim**

In case of CentOS, the commands below will work.
yum install vim
Lastly for Alpine:
apk update
apk add vim
If you want to directly write the commands in the Dockerfile:
FROM ubuntu

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
