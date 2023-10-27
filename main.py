# Import necessary libraries and modules
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from linkedin_data_transformer.linkedin_data_processor import scrape_linkedin_profile
from Output_parsers import person_intel_parser, PersonIntel
from agent.linkedin_agent import lookup
from typing import Tuple

name = ""


def main(name: str) -> Tuple[PersonIntel, str]:
    # Lookup the LinkedIn profile URL for the given name
    linkedin_profile_url = lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)


    summary_template = """
         given the Linkedin information {linkedin_information} about a person from I want you to create:
         1. a short summary
         2. two interesting facts about them
         3. A topic that may interest them
         4. 2 creative Ice breakers to open a conversation with them
        \n{format_instructions}
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    result = chain.run(linkedin_information=linkedin_data)
    return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url")



