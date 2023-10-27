
# LinkedIn Profile Summarizer

## Overview
This project provides a tool to search for a person's LinkedIn profile using their name, scrapes the profile data, and then summarizes the profile. The summarized profile is presented in a user-friendly format using Flask, allowing users to view the summary without needing to interact directly with the console.

## Configuration
1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Set up the required API keys in a `.env` file (rename from `.env.template` if needed).

## Required API Keys
You'll need to obtain and set up the following API keys:
- `OPENAI_API_KEY`: For interacting with the OpenAI API.
- `PROXYCURL_API_KEY`: Used for scraping LinkedIn profile data.
- `SERPAPI_API_KEY`: Required for searching LinkedIn profiles using Google search.

Place these keys in a `.env` file (rename from `.env.template` if needed) in the root directory.

---

For more details on specific functionalities, refer to the respective module's comments and documentation.refer to the respective module's comments and documentation.

For more details about langchain, you can [read the documentation here](https://python.langchain.com/docs/get_started/introduction).
refer to the respective module's comments and documentation.

