import requests 
from app.config import GITHUB_TOKEN, URL_GITHUB_API


header = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_repositories():
    response = requests.get(
        f"{URL_GITHUB_API}/user/repos",
        headers = header
    )

    return response.json()

def get_organizations():
    response = requests.get(
        f"{URL_GITHUB_API}/user/orgs",
        headers = header
    )

    return response.json()

def get_pull_requests(username):
    response = requests.get(
        f"{URL_GITHUB_API}/search/issues?q=author:{username}+type:pr",
        headers= header
    )

    return response.json()["items"]