from langchain_community.tools.tavily_search import TavilySearchResults #Search-Engine API optimised for LLM workloads

def get_profile_url_tavily(query:str):
    """Searches for LinkedIn or Twitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{query}")
    return res