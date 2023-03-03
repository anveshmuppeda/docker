# Commit Image:  
First, we commit the changes with the command:

```docker commit nginx-base```   

What this will do is create a new image without a repository or tag.   

Notice that it doesn’t have either a REPOSITORY (the first column) or a TAG (the second column).  
For this image to be usable, we have to tag it.  
In order to tag the image, we have to use the IMAGE ID as an identifier, so tag the image like this:  
```
docker tag IMAGE_ID <image-name>:<tag>
```
Where IMAGE_ID is the actual ID of your new container.

Now, if you list the images (using the docker images command), you’ll see something like this:

