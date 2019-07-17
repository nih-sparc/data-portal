.PHONY: help all serve clean install

all: clean serve ## Cleans and starts the application

clean: ## Cleans generated files
		rm -rf **/*/dist/

serve: ## Serves the application in dev mode, reachable from your network
		FLASK_DEBUG=1 FLASK_ENV=development flask run --host=0.0.0.0

install: ## Install virtual environment and requirements
		python3 -m venv venv
		venv/bin/pip install -U pip setuptools wheel
		venv/bin/pip install -r requirements.txt
		@echo "To activate the venv, execute 'source venv/bin/activate' or 'venv/Scripts/activate.bat' (WIN)"

# HELP
# This will output the prefixed ## comments of each task as a help
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help: ## This help
		@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
