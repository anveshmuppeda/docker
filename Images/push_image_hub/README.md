

# Docker Image Push to Docker Hub

Login to the docker.

docker login -u sirimalla

Tag your image build

my image name here is : mylocalimage and by default it has tag : latest
and my username is : sirimalla as registered with docker cloud, and I created a public repository named : dockerhub

so my personal repository becomes now : sirimalla/dockerhub and I want to push my image with tag : myfirstimagepush

I tagged as below :

docker tag mylocalimage:latest sirimalla/dockerhub:myfirstimagepush
Pushed the image to my personal docker repository as below

docker push sirimalla/dockerhub:myfirstimagepush

And it successfully pushed to my personal docker repo.
