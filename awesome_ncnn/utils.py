"""Utility functions for the Awesome NCNN Collection."""

from __future__ import annotations

import re

from pathlib import Path


def read_markdown_file(file_path: str | Path) -> str:
    """Read a markdown file and return its contents.

    Args:
        file_path: Path to the markdown file.

    Returns:
        Contents of the markdown file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a markdown file.

    Examples:
        >>> content = read_markdown_file("README.md")
        >>> len(content) > 0
        True
    """
    path = Path(file_path)

    if not path.exists():
        msg = f"File not found: {file_path}"
        raise FileNotFoundError(msg)

    if path.suffix.lower() not in {".md", ".markdown"}:
        msg = f"File is not a markdown file: {file_path}"
        raise ValueError(msg)

    return path.read_text(encoding="utf-8")


def extract_links_from_markdown(content: str) -> list[str]:
    """Extract all links from markdown content.

    Args:
        content: The markdown content.

    Returns:
        List of URLs found in the markdown content.

    Examples:
        >>> extract_links_from_markdown("[link](https://example.com)")
        ['https://example.com']
    """
    # Markdown link pattern: [text](url)
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(pattern, content)
    return [url for _, url in matches]


def get_project_root() -> Path:
    """Get the root directory of the project.

    Returns:
        Path to the project root directory.

    Examples:
        >>> root = get_project_root()
        >>> root.exists()
        True
    """
    current = Path.cwd()

    # Look for pyproject.toml or .git directory
    for parent in [current, *current.parents]:
        if (parent / "pyproject.toml").exists() or (parent / ".git").exists():
            return parent

    return current


def format_github_stars(stars: int) -> str:
    """Format GitHub stars count for display.

    Args:
        stars: Number of stars.

    Returns:
        Formatted string representation.

    Examples:
        >>> format_github_stars(1234)
        '1.2k'
        >>> format_github_stars(1234567)
        '1.2M'
        >>> format_github_stars(123)
        '123'
    """
    million = 1_000_000
    thousand = 1_000

    if stars >= million:
        return f"{stars / million:.1f}M"
    if stars >= thousand:
        return f"{stars / thousand:.1f}k"
    return str(stars)
