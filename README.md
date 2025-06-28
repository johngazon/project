# Local Assistant Agent

This project provides a simple local agent using the `deepseek-coder-v2:latest` model with [Ollama](https://ollama.com/). The agent exposes a web API via **FastAPI** so it can be reached from any device on your local network.

## Features

- DuckDuckGo web search
- Wikipedia summaries
- Current date retrieval
- Read files and list directories
- Ask clarifying questions to the user

## Requirements

- Python 3.11+
- [Ollama](https://ollama.com/) installed locally and the `deepseek-coder-v2:latest` model pulled.

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Pull the model if needed:

```bash
ollama pull deepseek-coder-v2:latest
```

## Running

Start the server so it listens on all network interfaces:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Send a POST request to `http://<your-ip>:8000/chat` with a JSON body:

```json
{ "message": "Who won the last world cup?" }
```

The response will contain the agent's answer.
