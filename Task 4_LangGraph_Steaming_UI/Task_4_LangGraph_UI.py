import os
from typing import TypedDict
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from dotenv import load_dotenv

load_dotenv()


# Initialise LLM
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model= "gpt-3.5-turbo", temperature=0.9, api_key=api_key)


# Define the state
class AgentState (TypedDict):
    topic: str
    joke: str


# Node
def joke_node(state: AgentState) -> AgentState:
    """A node to generate a joke"""
    topic = state.get("topic", "anything")
    prompt = f"Tell me a short, funny, family-friendly joke about {topic}."

    response = llm.invoke([HumanMessage(content=prompt)])
    state["joke"] = response.content
    return state


# Building a graph
def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("generate_joke", joke_node)
    builder.set_entry_point("generate_joke")
    builder.set_finish_point("generate_joke")

    return builder.compile()