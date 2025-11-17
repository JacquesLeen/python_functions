"""Tests for the wikibot module."""

from wikibot import get_wikipedia_summary

def test_get_wikipedia_summary():
    """Test get_wikipedia_summary to ensure it returns a valid summary."""
    topic = "Python (programming language)"
    summary = get_wikipedia_summary(topic, sentences=2)
    assert isinstance(summary, str)
    assert len(summary) > 0
    assert "Python" in summary
