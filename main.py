# Import necessary libraries and modules
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import linkedin_data_transformer.linkedin_data_processor as linkedin_processor
from Output_parsers import person_intel_parser
from agent.linkedin_agent import lookup

name = ""


def main(name: str):
    # Lookup the LinkedIn profile URL for the given name
    linkedin_profile_url = lookup(name=name)

    # Define the template for generating the summary
    summary_template = """
    given the information {information} about a person, I want you to create:
    1. a short summary
    2. two interesting facts about them
    3. A topic that may interest them
            \n{format_instructions}
    """

    # Create a prompt template based on the summary template
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    # Initialize the ChatOpenAI model and LLMChain for generating the summary
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # Scrape the LinkedIn profile data
    linkedin_data = linkedin_processor.scrape_linkedin_profile(linkedin_profile_url)

    # Print the generated summary based on the scraped LinkedIn data
    result = chain.run(information=linkedin_data)

    return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    main()
