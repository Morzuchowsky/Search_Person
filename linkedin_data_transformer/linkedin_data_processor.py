import os
import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_linkedin_profile(linkedin_profile_url: str) -> dict:
    """Fetch information from a LinkedIn profile using the Proxycurl API."""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    headers = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=headers
    )
    response.raise_for_status()
    return response.json()


def clean_linkedin_data(data: dict) -> dict:
    """Clean and filter specific fields from LinkedIn profile data."""
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", None) and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data["groups"]:
            group_dict.pop("profile_pic_url", None)
    return data


def scrape_linkedin_profile(linkedin_profile_url: str) -> dict:
    """Scrape and clean information from a LinkedIn profile."""
    raw_data = fetch_linkedin_profile(linkedin_profile_url)
    return clean_linkedin_data(raw_data)
