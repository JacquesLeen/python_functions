"""Tests for the wikibot module."""

from wikibot import get_wikipedia_summary
from click.testing import CliRunner


def test_get_wikipedia_summary():
    """Test get_wikipedia_summary to ensure it returns a valid summary."""
    runner = CliRunner()
    result = runner.invoke(get_wikipedia_summary, ["--name", "Python (programming language)", "--sentences", "3"])
    assert "Python" in result.output
    assert isinstance(result.output, str)
    assert len(result.output) > 0

