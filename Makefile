CONTAINER_NAME=tor
BUILD=ryaben/torc
PORT=9050

.PHONY: up down

up:
        docker run \
        --rm \
        --detach \
        --name $(CONTAINER_NAME) \
        --publish $(PORT):$(PORT) \
        $(BUILD)

down:
	docker stop $(CONTAINER_NAME) 