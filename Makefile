.PHONY: build run

DOCKERFILE=Dockerfile
IMAGE_NAME=talk-time-app

build: ## Docker build
	docker build -t $(IMAGE_NAME) .

run: ## Docker run
	source .env && docker run --rm -e DISCORD_TOKEN=$$DISCORD_TOKEN $(IMAGE_NAME)

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\t\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
