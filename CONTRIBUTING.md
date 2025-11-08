# Contributing to Awesome NCNN Collection

Thank you for your interest in contributing! 🎉

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Quality](#code-quality)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Style Guide](#style-guide)

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- [Hatch](https://hatch.pypa.io/) (recommended) or pip

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR_USERNAME/awesome-ncnn-collection.git
cd awesome-ncnn-collection
```

---

## Development Setup

We use **Hatch** as our project manager. It handles virtual environments, dependencies, and scripts automatically.

### Option 1: Using Hatch (Recommended)

```bash
# Install Hatch
pip install hatch

# Install pre-commit hooks
hatch run pre-commit-install

# Run all checks
hatch run all
```

### Option 2: Using pip

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

---

## Code Quality

We use multiple tools to ensure code quality:

### 🔍 Linting with Ruff

```bash
# Run linter
hatch run lint

# Auto-fix issues
hatch run ruff check --fix .
```

### 🎨 Formatting with Black

```bash
# Check formatting
hatch run format-check

# Format code
hatch run format
```

### 🔎 Type Checking with MyPy

```bash
# Run type checker
hatch run type-check
```

### ✅ Run All Quality Checks

```bash
# Run all checks at once
hatch run check
```

---

## Testing

### Running Tests

```bash
# Run all tests
hatch run test

# Run with coverage
hatch run test-cov

# Run in parallel
hatch run test-parallel

# Run specific test
hatch run test tests/test_specific.py

# Run tests matching pattern
hatch run test -k "test_pattern"
```

### Coverage Reports

```bash
# Generate coverage report
hatch run cov-report

# Generate HTML coverage report
hatch run cov-html
# Open htmlcov/index.html in browser
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Name test functions `test_*`
- Use descriptive test names
- Add docstrings to complex tests

Example:

```python
def test_example_function():
    """Test that example_function returns expected result."""
    result = example_function(input_data)
    assert result == expected_output
```

---

## Submitting Changes

### Pre-commit Hooks

Before committing, pre-commit hooks will automatically run:

```bash
# Run pre-commit manually on all files
hatch run pre-commit-run

# Update pre-commit hooks
hatch run pre-commit-update
```

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new YOLO implementation
fix: correct version parsing
docs: update installation guide
style: format code with black
test: add tests for new feature
refactor: simplify configuration parsing
chore: update dependencies
```

### Pull Request Process

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and commit:
   ```bash
   git add .
   git commit -m "feat: your feature description"
   ```

3. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request** on GitHub

5. **Wait for review**:
   - CI checks must pass
   - Code review approval required
   - Address any feedback

---

## Style Guide

### Python Code Style

We follow [PEP 8](https://pep8.org/) with these specific guidelines:

#### Line Length
- Maximum 100 characters (enforced by Black and Ruff)

#### Imports
```python
# Standard library
import os
import sys

# Third-party
import requests
import yaml

# Local
from awesome_ncnn import utils
```

#### Type Hints
```python
def process_data(items: list[str]) -> dict[str, int]:
    """Process items and return counts."""
    return {item: len(item) for item in items}
```

#### Docstrings
Use Google-style docstrings:

```python
def example_function(param1: str, param2: int = 0) -> bool:
    """Short description of function.

    Longer description if needed.

    Args:
        param1: Description of param1.
        param2: Description of param2. Defaults to 0.

    Returns:
        Description of return value.

    Raises:
        ValueError: If param1 is empty.

    Example:
        >>> example_function("test", 5)
        True
    """
    if not param1:
        raise ValueError("param1 cannot be empty")
    return len(param1) > param2
```

### Markdown Style

- Use ATX-style headers (`#` not `===`)
- Add blank lines around headers
- Use fenced code blocks with language specifiers
- Limit line length to 100 characters
- Use reference-style links for repeated URLs

### YAML Style

- Use 2 spaces for indentation
- Use lowercase for keys
- Quote strings when necessary
- Add comments for complex configurations

---

## Additional Resources

### Documentation

```bash
# Build documentation
hatch run docs:build

# Serve documentation locally
hatch run docs:serve
```

### Hatch Commands

```bash
# List all environments
hatch env show

# Create new environment
hatch env create

# Remove environment
hatch env remove default

# Run command in environment
hatch run <script>
```

### Getting Help

- 📖 Read the [README](README.md)
- 💬 Open a [Discussion](https://github.com/umitkacar/awesome-ncnn-collection/discussions)
- 🐛 Report [Issues](https://github.com/umitkacar/awesome-ncnn-collection/issues)
- 📧 Contact maintainers

---

## Code of Conduct

Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing! 🙏**
