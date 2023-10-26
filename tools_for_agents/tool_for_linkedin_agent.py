# Import necessary libraries and modules
from langchain.utilities.serpapi import SerpAPIWrapper
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from langchain.utilities import SerpAPIWrapper


class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self):
        super(CustomSerpAPIWrapper, self).__init__()

    @staticmethod
    def _process_response(res: dict) -> str:
        """Process response from SerpAPI."""
        if "error" in res.keys():
            raise ValueError(f"Got error from SerpAPI: {res['error']}")
        if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
            toret = res["answer_box"]["answer"]
        elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
            toret = res["answer_box"]["snippet"]
        elif (
                "answer_box" in res.keys()
                and "snippet_highlighted_words" in res["answer_box"].keys()
        ):
            toret = res["answer_box"]["snippet_highlighted_words"][0]
        elif (
                "sports_results" in res.keys()
                and "game_spotlight" in res["sports_results"].keys()
        ):
            toret = res["sports_results"]["game_spotlight"]
        elif (
                "knowledge_graph" in res.keys()
                and "description" in res["knowledge_graph"].keys()
        ):
            toret = res["knowledge_graph"]["description"]
        elif "snippet" in res["organic_results"][0].keys():
            toret = res["organic_results"][0]["link"]

        else:
            toret = "No good search result found"
        return toret


def search_linkedin_profile(text: str) -> str:
    """
    Search for a LinkedIn profile using the given text and return the result.

    Args:
    - text (str): The query text for searching the LinkedIn profile.

    Returns:
    - str: LinkedIn URL
    """
    search = CustomSerpAPIWrapper()
    res = search.run(text)
    return res
