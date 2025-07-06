import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")


url = "https://v3.football.api-sports.io/leagues"

payload={}
headers = {
  'x-rapidapi-key': api_key,
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
