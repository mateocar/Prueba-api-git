from fastapi import FastAPI, HTTPException
from app.config import GITHUB_TOKEN
from app.service import *

app = FastAPI(title="Prueba Tecnica")

@app.get("/github-info")

def get_info_github():

    #Validar que el TOKEN exista
    if not GITHUB_TOKEN:
        raise HTTPException(status_code=500, detail="Token no configurated")
    
    #obtener repositorios del usuario
    repos = get_repositories()

    #obtener organizaciones del usuario
    orgs =  get_organizations()

    #se obtiene el user name por lo repositorios
    if len(repos) > 0:
        username = repos[0]["owner"]["login"]
        pull_req = get_pull_requests(username)
    else:
        pull_req = []
    
    #respuesta en formato json
    response = {
        "repositories": [],
        "organizations": [],
        "pull_requests": []
    }

    #se guardan datos de los repositorios
    for repo in repos:
        response["repositories"].append({
            "name": repo["name"],
            "private": repo["private"]
        })
    
    #se guardan datos de las organizaciones
    for org in orgs:
        response["organizations"].append({
            "login": org["login"]
        })

    #se guardan datos de los pull requests
    for pr in pull_req:
        response["pull_requests"].append({
            "title": pr["title"],
            "state": pr["state"]
        })

    return response

