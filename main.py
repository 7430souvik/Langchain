from dotenv import load_dotenv


load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
       query: The query to search for
    Returns:
       The search result
    """
    print(f"Searching for {query}")
    return  tavliy.search(query=query) 
    




llm = ChatOllama(model="llama3.1:latest")
tools= [search]
agent = create_agent(model= llm, tools=tools)


def main():
    print("Hello from search-agent!")
    result= agent.invoke({"messages": HumanMessage(content= "what is the weather in India")})
    print(result)


if __name__ == "__main__":
    main()
