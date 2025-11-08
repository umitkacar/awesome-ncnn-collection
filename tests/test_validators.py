"""Tests for validators module."""

from __future__ import annotations

from awesome_ncnn.validators import (
    validate_github_url,
    validate_resource,
    validate_url,
)


class TestValidateUrl:
    """Tests for validate_url function."""

    def test_valid_https_url(self) -> None:
        """Test validation of valid HTTPS URLs."""
        assert validate_url("https://github.com/Tencent/ncnn")
        assert validate_url("https://www.google.com")
        assert validate_url("https://example.com/path/to/resource")

    def test_valid_http_url(self) -> None:
        """Test validation of valid HTTP URLs."""
        assert validate_url("http://example.com")
        assert validate_url("http://localhost:8000")

    def test_invalid_url(self) -> None:
        """Test validation of invalid URLs."""
        assert not validate_url("not a url")
        assert not validate_url("ftp://example.com")
        assert not validate_url("")
        assert not validate_url("github.com")


class TestValidateGithubUrl:
    """Tests for validate_github_url function."""

    def test_valid_github_url(self) -> None:
        """Test validation of valid GitHub URLs."""
        assert validate_github_url("https://github.com/Tencent/ncnn")
        assert validate_github_url("https://github.com/user/repo")

    def test_invalid_github_url(self) -> None:
        """Test validation of non-GitHub URLs."""
        assert not validate_github_url("https://google.com")
        assert not validate_github_url("not a url")
        assert not validate_github_url("https://gitlab.com/project")


class TestValidateResource:
    """Tests for validate_resource function."""

    def test_valid_resource(self) -> None:
        """Test validation of valid resources."""
        resource = {
            "name": "ncnn",
            "url": "https://github.com/Tencent/ncnn",
        }
        assert validate_resource(resource)

    def test_resource_without_url(self) -> None:
        """Test validation of resource without URL."""
        resource = {"name": "ncnn"}
        assert validate_resource(resource)

    def test_invalid_resource_no_name(self) -> None:
        """Test validation fails when name is missing."""
        resource = {"url": "https://github.com/Tencent/ncnn"}
        assert not validate_resource(resource)

    def test_invalid_resource_empty_name(self) -> None:
        """Test validation fails when name is empty."""
        resource = {"name": "", "url": "https://github.com/Tencent/ncnn"}
        assert not validate_resource(resource)

    def test_invalid_resource_invalid_url(self) -> None:
        """Test validation fails when URL is invalid."""
        resource = {"name": "ncnn", "url": "not a url"}
        assert not validate_resource(resource)

    def test_invalid_resource_not_dict(self) -> None:
        """Test validation fails when input is not a dictionary."""
        assert not validate_resource("not a dict")  # type: ignore[arg-type]
        assert not validate_resource([])  # type: ignore[arg-type]
        assert not validate_resource(None)  # type: ignore[arg-type]
