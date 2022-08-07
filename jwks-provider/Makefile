IMAGE_NAME=jwks-provider
CONTAINER_NAME=jwks-provider
INTERNAL_PORT=8010
WORKERS=2

USER_ID?=$(shell id -u)
SERVICE_NAME=jwks-provider


run:
	@uvicorn \
    	service.main:app \
    	--host 0.0.0.0 \
    	--port $(INTERNAL_PORT) \
    	--reload

clean:
	@echo "> Removing container $(CONTAINER_NAME)"
	- @docker rm $(CONTAINER_NAME)
	@echo "> Removing image $(CONTAINER_NAME)"
	- @docker image rm $(CONTAINER_NAME)


build:
	@docker \
		build . \
			--build-arg INTERNAL_PORT=$(INTERNAL_PORT) \
			--build-arg WORKERS=$(WORKERS) \
			-t $(CONTAINER_NAME)


clean-build:
	make clean
	make build
