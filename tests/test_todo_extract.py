"""Tests for todo-extract."""

import pytest
from todo_extract import extract


class TestExtract:
    """Test suite for extract."""

    def test_basic(self):
        """Test basic usage."""
        result = extract("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            extract("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = extract(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
