# Development Guide

Complete guide for developers working on the Awesome NCNN Collection project.

## Table of Contents

- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Tools & Configuration](#tools--configuration)
- [CI/CD Pipeline](#cicd-pipeline)
- [Troubleshooting](#troubleshooting)

---

## Quick Start

### 1. Install Hatch

```bash
# Using pip
pip install hatch

# Using pipx (recommended)
pipx install hatch

# Using Homebrew (macOS)
brew install hatch
```

### 2. Clone and Setup

```bash
git clone https://github.com/umitkacar/awesome-ncnn-collection.git
cd awesome-ncnn-collection
hatch env create
hatch run pre-commit-install
```

### 3. Run Quality Checks

```bash
# Run all checks and tests
hatch run all
```

---

## Project Structure

```
awesome-ncnn-collection/
├── .github/
│   └── workflows/
│       ├── ci.yml              # CI/CD pipeline
│       └── release.yml         # Release workflow
├── docs/                       # Documentation
├── tests/                      # Test files
│   ├── __init__.py
│   ├── test_example.py
│   └── conftest.py
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── pyproject.toml              # Project configuration
├── README.md                   # Project readme
├── CONTRIBUTING.md             # Contribution guide
├── DEVELOPMENT.md              # This file
└── LICENSE                     # MIT License
```

---

## Development Workflow

### Daily Development

```bash
# 1. Create feature branch
git checkout -b feature/my-feature

# 2. Make changes
# ... edit files ...

# 3. Run quality checks
hatch run check

# 4. Run tests
hatch run test-cov

# 5. Commit (pre-commit hooks run automatically)
git commit -m "feat: add new feature"

# 6. Push
git push origin feature/my-feature
```

### Available Hatch Scripts

#### Quality Checks

```bash
# Linting
hatch run lint                  # Run Ruff linter
hatch run ruff check --fix .    # Auto-fix linting issues

# Formatting
hatch run format                # Format with Black
hatch run format-check          # Check formatting without changes

# Type Checking
hatch run type-check            # Run MyPy type checker

# All Checks
hatch run check                 # Run all quality checks
```

#### Testing

```bash
# Basic testing
hatch run test                  # Run all tests
hatch run test-cov              # Run with coverage
hatch run test-parallel         # Run tests in parallel

# Coverage
hatch run cov-report            # Show coverage report
hatch run cov-html              # Generate HTML coverage report

# Specific tests
hatch run test tests/test_specific.py
hatch run test -k "test_pattern"
hatch run test -m "slow"        # Run marked tests
```

#### Pre-commit

```bash
# Installation
hatch run pre-commit-install    # Install hooks

# Manual execution
hatch run pre-commit-run        # Run on all files

# Maintenance
hatch run pre-commit-update     # Update hook versions
```

#### Documentation

```bash
hatch run docs:build            # Build documentation
hatch run docs:serve            # Serve docs locally
```

#### Combined

```bash
hatch run all                   # Run all checks + tests
```

---

## Tools & Configuration

### Ruff - Fast Python Linter

**Configuration:** `[tool.ruff]` in `pyproject.toml`

Features:

- ⚡ 10-100x faster than traditional linters
- 🎯 Replaces Flake8, isort, pydocstyle, pyupgrade
- 🔧 Auto-fixes many issues
- 📊 Comprehensive rule set

```bash
# Check all files
ruff check .

# Auto-fix issues
ruff check --fix .

# Show statistics
ruff check --statistics .

# Check specific rules
ruff check --select E,F .
```

### Black - Code Formatter

**Configuration:** `[tool.black]` in `pyproject.toml`

Features:

- 🎨 Uncompromising code formatter
- ⚙️ Line length: 100 characters
- 🔄 Consistent style across codebase

```bash
# Format all files
black .

# Check without modifying
black --check .

# Show diff
black --diff .

# Format specific file
black path/to/file.py
```

### MyPy - Static Type Checker

**Configuration:** `[tool.mypy]` in `pyproject.toml`

Features:

- 🔍 Static type checking
- 📝 Catches type errors before runtime
- ✅ Strict mode enabled

```bash
# Check all files
mypy .

# Check specific file
mypy path/to/file.py

# Show error codes
mypy --show-error-codes .

# Verbose output
mypy --verbose .
```

### Pytest - Testing Framework

**Configuration:** `[tool.pytest.ini_options]` in `pyproject.toml`

Features:

- 🧪 Powerful testing framework
- 📊 Coverage integration
- 🔀 Parallel execution support
- 🏷️ Test markers (unit, integration, slow)

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run in parallel
pytest -n auto

# Run specific marker
pytest -m unit
pytest -m "not slow"

# Verbose output
pytest -v

# Stop on first failure
pytest -x

# Show local variables on failure
pytest -l
```

### Coverage - Code Coverage

**Configuration:** `[tool.coverage]` in `pyproject.toml`

Features:

- 📊 Branch coverage enabled
- 📈 HTML and XML reports
- 🎯 Minimum coverage thresholds

```bash
# Run with coverage
pytest --cov

# Generate report
coverage report

# Generate HTML report
coverage html
# Open htmlcov/index.html

# Generate XML report (for CI)
coverage xml

# Erase coverage data
coverage erase
```

### Pre-commit - Git Hooks

**Configuration:** `.pre-commit-config.yaml`

Hooks included:

- ✅ Ruff (linting + formatting)
- ✅ Black (formatting)
- ✅ MyPy (type checking)
- ✅ Bandit (security)
- ✅ Pydocstyle (docstring)
- ✅ YAML/JSON/TOML validators
- ✅ Trailing whitespace fixer
- ✅ End of file fixer
- ✅ Secret detection

```bash
# Install hooks
pre-commit install

# Run on all files
pre-commit run --all-files

# Run specific hook
pre-commit run ruff --all-files

# Update hooks
pre-commit autoupdate

# Skip hooks (not recommended)
git commit --no-verify
```

---

## CI/CD Pipeline

### GitHub Actions Workflows

#### CI Pipeline (`.github/workflows/ci.yml`)

Runs on:

- Push to main/master/develop
- Pull requests
- Manual trigger

Jobs:

1. **Code Quality**
   - Ruff linting
   - Black formatting check
   - MyPy type checking
   - Python 3.8-3.12 matrix

2. **Security**
   - Bandit security scan
   - Safety dependency check

3. **Tests**
   - Ubuntu, macOS, Windows
   - Python 3.8-3.12
   - Coverage upload to Codecov

4. **Pre-commit**
   - Run all pre-commit hooks

5. **Documentation**
   - Build docs

6. **Dependency Review** (PRs only)
   - Security review of dependencies

#### Release Pipeline (`.github/workflows/release.yml`)

Runs on:

- GitHub release published
- Manual trigger

Jobs:

1. **Build**
   - Build wheel and sdist
   - Store artifacts

2. **Publish to PyPI**
   - Upload to PyPI

3. **GitHub Release**
   - Sign packages
   - Upload to GitHub release

### Local CI Simulation

```bash
# Run same checks as CI
hatch run all

# Individual CI jobs
hatch run lint          # Quality: Linting
hatch run format-check  # Quality: Formatting
hatch run type-check    # Quality: Type checking
hatch run test-cov      # Tests with coverage
hatch run docs:build    # Documentation build
```

---

## Troubleshooting

### Common Issues

#### 1. Pre-commit Hook Failures

```bash
# Update hooks
pre-commit autoupdate

# Clear cache
pre-commit clean

# Reinstall
pre-commit uninstall
pre-commit install
```

#### 2. Type Checking Errors

```bash
# Ignore specific line
result = function()  # type: ignore[error-code]

# Ignore file
# mypy: ignore-errors

# Update stubs
pip install types-requests types-PyYAML
```

#### 3. Import Errors in Tests

```bash
# Reinstall in editable mode
pip install -e ".[dev]"

# Or with hatch
hatch env create
```

#### 4. Coverage Not Working

```bash
# Clear coverage data
coverage erase

# Run with coverage
pytest --cov --cov-report=term-missing

# Check coverage configuration
cat pyproject.toml | grep -A 10 "\[tool.coverage"
```

#### 5. Hatch Environment Issues

```bash
# Show environments
hatch env show

# Remove environment
hatch env remove default

# Recreate environment
hatch env create

# Prune unused environments
hatch env prune
```

### Getting Help

- 📖 [Hatch Documentation](https://hatch.pypa.io/)
- 📖 [Ruff Documentation](https://docs.astral.sh/ruff/)
- 📖 [Black Documentation](https://black.readthedocs.io/)
- 📖 [MyPy Documentation](https://mypy.readthedocs.io/)
- 📖 [Pytest Documentation](https://docs.pytest.org/)
- 💬 [GitHub Discussions](https://github.com/umitkacar/awesome-ncnn-collection/discussions)

---

## Best Practices

### 1. Before Committing

```bash
# Always run checks
hatch run all

# Or use pre-commit
pre-commit run --all-files
```

### 2. Writing Tests

- Write tests for new features
- Maintain >80% coverage
- Use descriptive test names
- Test edge cases
- Use fixtures for common setup

### 3. Type Hints

- Add type hints to all functions
- Use `from __future__ import annotations` for forward refs
- Import types from `typing` module
- Use `Any` sparingly

### 4. Documentation

- Update README for user-facing changes
- Add docstrings to public APIs
- Include examples in docstrings
- Keep CONTRIBUTING.md up to date

### 5. Dependencies

- Keep dependencies minimal
- Pin major versions only
- Test with minimum versions
- Update regularly but carefully

---

## Release Process

1. **Update version** in `pyproject.toml`
2. **Update CHANGELOG.md**
3. **Create git tag**

   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin v1.0.0
   ```

4. **Create GitHub release**
   - Triggers automatic PyPI upload
   - Generates signed artifacts

---

**Happy coding! 🚀**
