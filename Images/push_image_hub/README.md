

# Docker Image Push to Docker Hub

Login to the docker.  
```
docker login -u anvesh35  
```
Tag your image build  

my image name here is : ```mylocalimage``` and by default it has tag : ```latest```   
and my username is : ```anvesh35``` as registered with docker cloud,   
and I created a public repository named : ```dockerhub```   

so my personal repository becomes now : ```anvesh35/dockerhub``` and I want to push my image with tag : ```myfirstimagepush```  

I tagged as below :  

```docker tag mylocalimage:latest anvesh35/dockerhub:myfirstimagepush```  

Pushed the image to my personal docker repository as below
```
docker push anvesh35/dockerhub:myfirstimagepush
```

And it successfully pushed to my personal docker repo.
