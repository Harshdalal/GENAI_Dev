
The image contains a list of Docker commands, categorized into "IMAGES" and "CONTAINER".

IMAGES:

List all Local images: docker images
Delete an image: docker rmi <image_name>
Remove unused images: docker image prune
Build an image from a Dockerfile:
docker build -t <image_name>:<version> . (version is optional)
docker build -t <image_name>:<version> --no-cache (build without cache)

CONTAINER:

List all Local containers (running & stopped): docker ps -a
List all running containers: docker ps
Create & run a new container: docker run <image_name> (if image not available locally, it'll be downloaded from DockerHub)
Run container in background: docker run -d <image_name>
Run container with custom name: docker run --name <container_name> <image_name>
