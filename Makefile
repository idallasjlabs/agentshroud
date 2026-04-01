.PHONY: test lint fmt fmt-check build up down clean help

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

test:  ## Run test suite
	pytest gateway/tests/ -q --tb=short

test-cov:  ## Run tests with coverage report
	pytest gateway/tests/ --cov=gateway --cov-report=term-missing --cov-report=xml --cov-fail-under=94

lint:  ## Run ruff linter
	ruff check gateway/

fmt:  ## Format code with black
	black gateway/

fmt-check:  ## Check formatting without modifying files
	black --check gateway/

build:  ## Build Docker images
	docker compose -f docker/docker-compose.yml build

up:  ## Start stack (uses asb for ephemeral secrets)
	scripts/asb up

down:  ## Stop stack
	scripts/asb down

rebuild:  ## Rebuild and restart stack
	scripts/asb rebuild

clean:  ## Remove containers, prune volumes and build cache
	scripts/asb clean-rebuild

pre-commit:  ## Run all pre-commit hooks
	pre-commit run --all-files
