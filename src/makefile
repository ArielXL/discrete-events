.PHONY: clean

NAME 	   	:= Population Evolution
VERSION		:= 1.0
DEVELOPER 	:= Ariel Plasencia Díaz
COPYRIGHT  	:= Copyright © 2021: $(DEVELOPER)

run: ## Run the project :)
	python3 main.py

info: ## Display project description
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Show the project version
	@echo "$(NAME) v$(VERSION)"

install: ## Install the project dependencies
	pip3 install simpy
	pip3 install matplotlib

clean: ## Remove temporary files
	rm -rf __pycache__/

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'