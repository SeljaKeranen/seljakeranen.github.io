.DEFAULT_GOAL := help
VENV := .venv
PY := $(VENV)/bin/python

.PHONY: help install serve build test lint fmt new hooks clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN{FS=":.*?## "}{printf "  \033[1m%-10s\033[0m %s\n", $$1, $$2}'

install: ## Create the venv and install dev + doc dependencies
	uv venv $(VENV)
	$(VENV)/bin/pip install -r requirements-dev.txt

serve: ## Live preview at http://127.0.0.1:8000
	$(PY) -m mkdocs serve

build: ## Strict production build into site/
	$(PY) -m mkdocs build --strict

test: ## Run the test suite (strict build + frontmatter + design invariants)
	$(PY) -m pytest

lint: ## Ruff lint
	$(VENV)/bin/ruff check .

fmt: ## Ruff format
	$(VENV)/bin/ruff format .

new: ## Scaffold a post:  make new TITLE="Post title" CATEGORY=Notes
	$(PY) scripts/new_post.py "$(TITLE)" --category "$(CATEGORY)"

hooks: ## Install the pre-commit hooks
	$(VENV)/bin/pre-commit install

clean: ## Remove build output
	rm -rf site .cache
