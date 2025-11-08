"""Pytest configuration and fixtures."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest


if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def sample_data() -> dict[str, str]:
    """Provide sample test data.

    Returns:
        Sample dictionary data for testing.
    """
    return {
        "name": "awesome-ncnn-collection",
        "version": "1.0.0",
        "description": "NCNN resources collection",
    }


@pytest.fixture
def temp_file(tmp_path: Path) -> Path:
    """Create a temporary file for testing.

    Args:
        tmp_path: Pytest fixture providing temporary directory.

    Returns:
        Path to temporary file.
    """
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("test content")
    return file_path
