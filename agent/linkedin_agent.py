from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from tools_for_agents.tool_for_linkedin_agent import search_linkedin_profile


def initialize_linkedin_lookup_agent():
    """Initialize the agent to lookup LinkedIn profile."""

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile page",
            func=search_linkedin_profile,
            description="A tool to crawl Google for LinkedIn profile pages",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    return agent


def lookup(name: str) -> str:
    """Get LinkedIn profile URL based on the given name."""

    template = """
    given the full name {name_of_person} I want You to get me a link to their LinkedIn profile page.
    Your answer should only be a URL.
    """

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    agent = initialize_linkedin_lookup_agent()
    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    return linkedin_profile_url
