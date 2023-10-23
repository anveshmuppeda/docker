# Nginx  
## Running Nginx Docker Image on Ec2 machine    
Create a Nginx container by typing the following command:  
```
docker run -d -p 80:80 --name nginx nginx
```  
Run the docker’s command to confirm that an nginx container has been successfully created:  
```
docker ps -a  
```  

The last step is to visit the public DNS name in your browser


## Reference:  
https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-docker/