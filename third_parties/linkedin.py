import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles, manually scrape the infroamtion from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/JP-Thoma/9df16df0bb3caaa07ef8c65012f9a98a/raw/61ea69dfb3f0fcca4abb3eec816c2a543ed70251/jp-thoma-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10
        )
    
    data = response.json().get("person")

    #data = {
     #   k: v
      #  for k,v in data.items()
       # if v not in ([], "", "", None)
        #and k not in ["certifications"]}
    
    return data


if __name__=="__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://de.linkedin.com/in/jan-thoma"
        )
    )