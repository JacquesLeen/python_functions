"""FastAPI application for Wikipedia summaries."""

import uvicorn
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import wikipedia

from src.wikibot import fetch_wikipedia_summary

app = FastAPI()


class Wiki(BaseModel):
    """Request model for Wikipedia summary."""
    name: str
    sentences: int = 2


@app.get("/")
async def root():
    """Root endpoint with welcome message."""
    return {
        "message": "Welcome to the Wikipedia Summary API!",
        "endpoints": {
            "POST /wiki/": "Get a Wikipedia summary",
            "GET /docs": "API documentation"
        }
    }


@app.post("/wiki/")
async def wiki_summary(wiki: Wiki):
    """
    Fetch a Wikipedia summary for a given topic.
    
    Parameters:
    - name: Wikipedia page name
    - sentences: Number of sentences (default: 2)
    """
    try:
        summary = fetch_wikipedia_summary(wiki.name, sentences=wiki.sentences)
        return {"summary": summary}
    except wikipedia.exceptions.DisambiguationError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Ambiguous topic. Did you mean one of: {e.options[:5]}"
        )
    except wikipedia.exceptions.PageError:
        raise HTTPException(
            status_code=404,
            detail=f"Wikipedia page '{wiki.name}' not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred: {str(e)}"
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)