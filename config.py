from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

class Config:
    API_KEY: str = api_key
    API_SECRET: str = api_secret