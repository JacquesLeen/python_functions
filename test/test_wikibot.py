"""Tests for the wikibot module."""

from click.testing import CliRunner
from fastapi.testclient import TestClient
import pytest
import wikipedia
from main import app

from wikibot import get_wikipedia_summary, fetch_wikipedia_summary


# Tests for fetch_wikipedia_summary (core function)
def test_fetch_wikipedia_summary_valid():
    """Test fetch_wikipedia_summary with valid topic."""
    summary = fetch_wikipedia_summary("Python (programming language)")
    assert isinstance(summary, str)
    assert len(summary) > 0
    assert "Python" in summary


def test_fetch_wikipedia_summary_custom_sentences():
    """Test fetch_wikipedia_summary with custom sentences."""
    summary = fetch_wikipedia_summary("Python (programming language)", sentences=1)
    assert isinstance(summary, str)


def test_fetch_wikipedia_summary_invalid():
    """Test fetch_wikipedia_summary with invalid page."""
    with pytest.raises(wikipedia.exceptions.PageError):
        fetch_wikipedia_summary("xyzabc123notarealpage")


# Tests for Click CLI
def test_click_get_wikipedia_summary():
    """Test Click command."""
    runner = CliRunner()
    result = runner.invoke(
        get_wikipedia_summary, ["--name", "Python (programming language)"]
    )
    assert result.exit_code == 0
    assert "Python" in result.output


# Tests for FastAPI
@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


def test_api_root(client):
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]


def test_api_wiki_summary(client):
    """Test wiki summary endpoint."""
    response = client.post("/wiki/", json={"name": "Python (programming language)"})
    assert response.status_code == 200
    assert "summary" in response.json()
    assert "Python" in response.json()["summary"]


def test_api_wiki_custom_sentences(client):
    """Test wiki summary with custom sentences."""
    response = client.post(
        "/wiki/", json={"name": "Python (programming language)", "sentences": 1}
    )
    assert response.status_code == 200


def test_api_wiki_invalid_page(client):
    """Test wiki summary with invalid page."""
    response = client.post("/wiki/", json={"name": "xyzabc123notarealpage"})
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
