import os
from dotenv import load_dotenv

load_dotenv()

URL_GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GIT_HUB_TOKEN")