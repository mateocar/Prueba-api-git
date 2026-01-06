from pydantic import BaseModel
from typing import List

class Repository(BaseModel):
    name: str
    private: bool

class Organization(BaseModel):
    login: str

class PullRequest(BaseModel):
    title: str
    state: str

class GitResponse(BaseModel):
    respositories: List[Repository]
    organizations: List[Organization]
    pull_requests: List[PullRequest]