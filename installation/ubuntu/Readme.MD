# Install Docker on Linux  

If you are running Linux you will need to install Docker directly. You should be logged in as a user with sudo privileges. First, you will need to ensure that you have the command line utility cURL. Do this by opening a terminal and typing:
## Step 1  
```
$ which curl
```  
If cURL is not installed, update your package manager and install it, using:  

### Step 1.1 
```
$ sudo apt-get update
$ sudo apt-get install curl
```  
Now that you have cURL, you can use it to get the latest Docker package:  

## Step 2  
```
$ curl -fsSL https://get.docker.com/ | sh
```  

Add your account to the docker group.
## Step 3  
```
sudo usermod -aG docker <your_username>  
```
Replace <your_username>  with username like root.  
This step is required to be able to run Docker commands as a non-root user. You will have to log out and log back in for the change to take effect.  

Now you should have Docker! Verify that it is installed by running the hello-world container:  
## Step 4  
```
$ docker run hello-world  
```

Unable to find image 'hello-world:latest' locally  
latest: Pulling from library/hello-world  
b901d36b6f2f: Pull complete   
0a6ba66e537a: Pull complete   
Digest: sha256:8be990ef2aeb16dbcb9271ddfe2610fa6658d13f6dfb8bc72074cc1ca36966a7  
Status: Downloaded newer image for hello-world:latest  
Hello from Docker.  


This message shows that your installation appears to be working correctly.  

## Tip  
If you see the message "Cannot connect to the Docker daemon", you may need to restart the Docker service.  
```
$ sudo service docker restart  
```
  