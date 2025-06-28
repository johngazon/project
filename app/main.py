from fastapi import FastAPI
from pydantic import BaseModel

from .agent import create_agent

app = FastAPI(title="Local Assistant Agent")
agent = create_agent()


class Message(BaseModel):
    message: str


@app.post("/chat")
def chat(msg: Message):
    response = agent.run(msg.message)
    return {"response": response}
