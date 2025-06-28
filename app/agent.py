from langchain_community.llms import Ollama
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType

from . import tools


def create_agent():
    llm = Ollama(model="deepseek-coder-v2:latest")

    tool_list = [
        Tool(
            name="Search",
            func=tools.search_web,
            description="useful for when you need to answer questions about current events or the web",
        ),
        Tool(
            name="Wikipedia",
            func=tools.search_wikipedia,
            description="search Wikipedia for facts and summaries",
        ),
        Tool(
            name="CurrentDate",
            func=tools.get_current_date,
            description="returns today's date",
        ),
        Tool(
            name="ReadFile",
            func=tools.read_file,
            description="read a local file from disk",
        ),
        Tool(
            name="ListDir",
            func=tools.list_directory,
            description="list files in a directory",
        ),
        Tool(
            name="AskUser",
            func=tools.ask_user,
            description="ask the user for clarification",
        ),
    ]

    agent = initialize_agent(
        tool_list,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    return agent
