"""Tests for utils module."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest


if TYPE_CHECKING:
    from pathlib import Path

from awesome_ncnn.utils import (
    extract_links_from_markdown,
    format_github_stars,
    get_project_root,
    read_markdown_file,
)


class TestReadMarkdownFile:
    """Tests for read_markdown_file function."""

    def test_read_existing_markdown(self, tmp_path: Path) -> None:
        """Test reading an existing markdown file."""
        md_file = tmp_path / "test.md"
        md_file.write_text("# Test\nContent", encoding="utf-8")

        content = read_markdown_file(md_file)
        assert "# Test" in content
        assert "Content" in content

    def test_file_not_found(self) -> None:
        """Test error when file doesn't exist."""
        with pytest.raises(FileNotFoundError, match="File not found"):
            read_markdown_file("nonexistent.md")

    def test_not_markdown_file(self, tmp_path: Path) -> None:
        """Test error when file is not markdown."""
        txt_file = tmp_path / "test.txt"
        txt_file.write_text("Content", encoding="utf-8")

        with pytest.raises(ValueError, match="not a markdown file"):
            read_markdown_file(txt_file)


class TestExtractLinksFromMarkdown:
    """Tests for extract_links_from_markdown function."""

    def test_extract_single_link(self) -> None:
        """Test extracting a single link."""
        content = "[GitHub](https://github.com)"
        links = extract_links_from_markdown(content)
        assert links == ["https://github.com"]

    def test_extract_multiple_links(self) -> None:
        """Test extracting multiple links."""
        content = "[GitHub](https://github.com) and [Google](https://google.com)"
        links = extract_links_from_markdown(content)
        assert len(links) == 2
        assert "https://github.com" in links
        assert "https://google.com" in links

    def test_no_links(self) -> None:
        """Test when there are no links."""
        content = "Just some text without links"
        links = extract_links_from_markdown(content)
        assert links == []

    def test_complex_markdown(self) -> None:
        """Test with complex markdown."""
        content = """
        # Title
        Some text [link1](https://example.com/path)
        - [link2](https://github.com/user/repo)
        """
        links = extract_links_from_markdown(content)
        assert len(links) == 2


class TestGetProjectRoot:
    """Tests for get_project_root function."""

    def test_finds_project_root(self) -> None:
        """Test that it finds project root."""
        root = get_project_root()
        assert root.exists()
        # Should find either pyproject.toml or .git
        assert (root / "pyproject.toml").exists() or (root / ".git").exists()


class TestFormatGithubStars:
    """Tests for format_github_stars function."""

    def test_small_numbers(self) -> None:
        """Test formatting of small numbers."""
        assert format_github_stars(0) == "0"
        assert format_github_stars(123) == "123"
        assert format_github_stars(999) == "999"

    def test_thousands(self) -> None:
        """Test formatting of thousands."""
        assert format_github_stars(1_000) == "1.0k"
        assert format_github_stars(1_234) == "1.2k"
        assert format_github_stars(12_345) == "12.3k"

    def test_millions(self) -> None:
        """Test formatting of millions."""
        assert format_github_stars(1_000_000) == "1.0M"
        assert format_github_stars(1_234_567) == "1.2M"
        assert format_github_stars(12_345_678) == "12.3M"

    @pytest.mark.parametrize(
        ("stars", "expected"),
        [
            (0, "0"),
            (500, "500"),
            (1_500, "1.5k"),
            (22_000, "22.0k"),
            (2_500_000, "2.5M"),
        ],
    )
    def test_parametrized_formatting(self, stars: int, expected: str) -> None:
        """Test formatting with various inputs."""
        assert format_github_stars(stars) == expected
