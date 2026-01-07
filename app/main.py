from fastapi import FastAPI, HTTPException
from app.config import GITHUB_TOKEN
from app.service import *

app = FastAPI(title="Prueba Tecnica")

@app.get("/github-info")
def get_info_github():
    if not GITHUB_TOKEN:
        raise HTTPException(status_code=500, detail="Token no configurated")
    
    repos = get_repositories()
    orgs =  get_organizations()

    if len(repos) > 0:
        username = repos[0]["owner"]["login"]
        pull_req = get_pull_requests(username)
    else:
        pull_req = []
    
    response = {
        "repositories": [],
        "organizations": [],
        "pull_requests": []
    }

    for repo in repos:
        response["repositories"].append({
            "name": repo["name"],
            "private": repo["private"]
        })
    
    for org in orgs:
        response["organizations"].append({
            "login": org["login"]
        })

    for pr in pull_req:
        response["pull_requests"].append({
            "title": pr["title"],
            "state": pr["state"]
        })

    return response

