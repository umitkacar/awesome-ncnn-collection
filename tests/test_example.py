"""Example tests demonstrating testing patterns."""

from __future__ import annotations

import pytest


class TestExample:
    """Example test class."""

    def test_sample_data_fixture(self, sample_data: dict[str, str]) -> None:
        """Test using sample_data fixture.

        Args:
            sample_data: Fixture providing sample data.
        """
        assert sample_data["name"] == "awesome-ncnn-collection"
        assert sample_data["version"] == "1.0.0"

    def test_temp_file_fixture(self, temp_file) -> None:
        """Test using temp_file fixture.

        Args:
            temp_file: Fixture providing temporary file.
        """
        content = temp_file.read_text()
        assert content == "test content"
        assert temp_file.exists()


def test_simple_assertion() -> None:
    """Simple assertion test."""
    assert 1 + 1 == 2


def test_string_operations() -> None:
    """Test string operations."""
    text = "awesome-ncnn"
    assert text.startswith("awesome")
    assert text.endswith("ncnn")
    assert "ncnn" in text


@pytest.mark.parametrize(
    ("input_value", "expected"),
    [
        (1, 2),
        (2, 4),
        (3, 6),
        (4, 8),
    ],
)
def test_parametrized(input_value: int, expected: int) -> None:
    """Test with parametrization.

    Args:
        input_value: Input value to test.
        expected: Expected result.
    """
    assert input_value * 2 == expected


@pytest.mark.slow
def test_slow_operation() -> None:
    """Test marked as slow."""
    # This test is marked as slow
    # Run with: pytest -m slow
    # Skip with: pytest -m "not slow"
    assert True


@pytest.mark.unit
def test_unit_test() -> None:
    """Unit test example."""
    assert True


@pytest.mark.integration
def test_integration_test() -> None:
    """Integration test example."""
    assert True
