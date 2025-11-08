# GitHub Configuration

This directory contains GitHub-specific configuration files.

## GitHub Actions Workflows

Due to GitHub App permission requirements, workflow files cannot be pushed directly via API.

The following workflow files are available locally and should be added manually to the repository:

### Workflows to Add

1. **`.github/workflows/ci.yml`** - CI/CD Pipeline
   - Code quality checks (Ruff, Black, MyPy)
   - Security scanning (Bandit, Safety)
   - Multi-OS testing (Ubuntu, macOS, Windows)
   - Python 3.8-3.12 matrix
   - Pre-commit hook validation
   - Documentation build
   - Codecov integration

2. **`.github/workflows/release.yml`** - Release Automation
   - Package building
   - PyPI publishing
   - GitHub release creation
   - Artifact signing

### Manual Setup Instructions

To enable GitHub Actions:

1. Navigate to your repository on GitHub
2. Create `.github/workflows/` directory
3. Copy the workflow files from your local repository
4. Commit and push through the GitHub web interface or with appropriate permissions

### Alternative: Use GitHub Web Interface

You can also create workflows directly on GitHub:

1. Go to **Actions** tab in your repository
2. Click **New workflow**
3. Choose **set up a workflow yourself**
4. Copy content from local workflow files
5. Commit to repository

### Workflow Files Location

The complete workflow files are available in this directory locally:
- `workflows/ci.yml`
- `workflows/release.yml`

For full documentation on the CI/CD pipeline, see [DEVELOPMENT.md](../DEVELOPMENT.md).
