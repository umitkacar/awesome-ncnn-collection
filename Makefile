.PHONY: help install dev clean lint format type-check test test-cov pre-commit all docs

.DEFAULT_GOAL := help

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install the package
	pip install -e .

dev: ## Install development dependencies
	pip install -e ".[dev]"
	pre-commit install

clean: ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

lint: ## Run linting
	hatch run lint

format: ## Format code
	hatch run format

format-check: ## Check formatting
	hatch run format-check

type-check: ## Run type checker
	hatch run type-check

test: ## Run tests
	hatch run test

test-cov: ## Run tests with coverage
	hatch run test-cov

test-parallel: ## Run tests in parallel
	hatch run test-parallel

cov-report: ## Show coverage report
	hatch run cov-report

cov-html: ## Generate HTML coverage report
	hatch run cov-html

pre-commit: ## Run pre-commit on all files
	hatch run pre-commit-run

pre-commit-update: ## Update pre-commit hooks
	hatch run pre-commit-update

check: ## Run all quality checks
	hatch run check

all: ## Run all checks and tests
	hatch run all

docs-build: ## Build documentation
	hatch run docs:build

docs-serve: ## Serve documentation locally
	hatch run docs:serve

build: ## Build package
	hatch build

publish: ## Publish to PyPI
	hatch publish

version: ## Show version
	@python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])"
