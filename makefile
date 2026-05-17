image_name:=local-rag
tag:=test
dev_dockerfile = .devcontainer/Dockerfile
container_project_dir:=/home/my_project
host_project_dir:=/home/sileyeba/Projects/local_rag

init:
	docker build -t $(image_name):$(tag) -f $(dev_dockerfile) .

shell:
	docker run --rm -it -v $(PWD):/workspace -w /workspace $(image_name):$(tag) /bin/bash

clean:
	docker rmi -f $(image_name):$(tag)
