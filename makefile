help: ## show help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[$$()% a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

build: ## build python
	rm -rf package; \
	cd function; \
	pip install --target ../package/python -r requirements.txt; \
	cd ..

deploy: ## deploy infra
	bash scripts/build-deploy.sh

build-deploy: build deploy ## build and deploy infra

clean-up: ## clean up
	bash scripts/clean-up.sh

lambda-invoke: ## run integration smoke test
	bash scripts/lambda-invoke.sh

unit-test: ## run unit-test
	python3 function/lambda_function.test.py
