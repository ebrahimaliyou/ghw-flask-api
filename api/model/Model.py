from typing import TypedDict
from bson import ObjectId

'''
    @ class User : Schema for User collection
    @ class Project : Schema for Project collection
    @ class Task : Schema for Task collection
    @ class Issue : Schema for Issue collection
'''

class User(TypedDict):
    name: str
    skills: list[str]
    email: str

# status: "started", "in-progress", "completed
class Project(TypedDict):
    name: str
    description: str
    status: str
    created_at: str
    updated_at: str

# status: "started", "in-progress", "completed
class Task(TypedDict):
    project_id_ref: ObjectId
    name: str
    description: str
    status: str
    user_ids: list[str]
    created_at: str
    updated_at: str

# status: "started", "in-progress", "completed
class Issue(TypedDict):
    task_id_ref: ObjectId
    issue_tag: str
    status: str
    priority: str
    user_id: ObjectId
    created_at: str
    updated_at: str

