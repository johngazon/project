import os
from datetime import date
from duckduckgo_search import DDGS
import wikipedia


def search_web(query: str, max_results: int = 5) -> str:
    """Search the web using DuckDuckGo and return snippets."""
    results = []
    with DDGS() as ddgs:
        for result in ddgs.text(query, max_results=max_results):
            results.append(result.get("body", ""))
    return "\n".join(results)


def search_wikipedia(query: str) -> str:
    """Return a short summary from Wikipedia."""
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception as err:
        return f"Wikipedia error: {err}"


def get_current_date(_: str = "") -> str:
    """Return today's date as a string."""
    return str(date.today())


def read_file(path: str) -> str:
    """Read a local text file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as err:
        return f"File error: {err}"


def list_directory(path: str) -> str:
    """List files in a directory."""
    try:
        return "\n".join(os.listdir(path))
    except Exception as err:
        return f"Directory error: {err}"


def ask_user(question: str) -> str:
    """Return a clarification question for the user."""
    return f"Agent asks: {question}"
