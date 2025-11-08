"""Validators for NCNN resource links and data."""

from __future__ import annotations

import re

from typing import Any


def validate_url(url: str) -> bool:
    """Validate if a string is a valid URL.

    Args:
        url: The URL string to validate.

    Returns:
        True if the URL is valid, False otherwise.

    Examples:
        >>> validate_url("https://github.com/Tencent/ncnn")
        True
        >>> validate_url("not a url")
        False
    """
    url_pattern = re.compile(
        r"^https?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|"  # domain
        r"localhost|"  # localhost
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return bool(url_pattern.match(url))


def validate_github_url(url: str) -> bool:
    """Validate if a string is a valid GitHub URL.

    Args:
        url: The URL string to validate.

    Returns:
        True if the URL is a valid GitHub URL, False otherwise.

    Examples:
        >>> validate_github_url("https://github.com/Tencent/ncnn")
        True
        >>> validate_github_url("https://google.com")
        False
    """
    if not validate_url(url):
        return False
    return "github.com" in url.lower()


def validate_resource(resource: dict[str, Any]) -> bool:
    """Validate a resource dictionary.

    Args:
        resource: Dictionary containing resource information.

    Returns:
        True if the resource is valid, False otherwise.

    Examples:
        >>> validate_resource({"name": "ncnn", "url": "https://github.com/Tencent/ncnn"})
        True
        >>> validate_resource({"name": ""})
        False
    """
    if not isinstance(resource, dict):
        return False

    if "name" not in resource or not resource["name"]:
        return False

    return not ("url" in resource and not validate_url(resource["url"]))
