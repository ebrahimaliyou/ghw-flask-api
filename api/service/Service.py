from pymongo import MongoClient
from api.model.Model import User, Project, Task, Issue
from bson import ObjectId
from dotenv import load_dotenv
import os

config = load_dotenv()
PASSWORD = os.getenv("PASSWORD")

try:
    client = MongoClient("mongodb+srv://root:%s@cluster0.yumdxcu.mongodb.net/?retryWrites=true&w=majority"%PASSWORD)
    print("Connected to MongoDB")
except Exception as e:
    print(e)

db = client.projectCollaboration
projectCollection = db.projects
taskCollection = db.tasks
issueCollection = db.issues
userCollection = db.users

# user model crud functions
def get_user(user_id: str) -> User:
    user = userCollection.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise Exception("User not found")
    return user

def create_user(user: User):
    res = userCollection.insert_one(user)
    return res.inserted_id

def update_user(user_id: str, user: User):
    res = userCollection.update_one({"_id": ObjectId(user_id)}, {"$set": user})
    return res.acknowledged

def delete_user(user_id: str):
    res = userCollection.delete_one({"_id": ObjectId(user_id)})
    return res.acknowledged


# project model crud functions
def get_project(project_id: str):
    project = projectCollection.find_one({"_id": ObjectId(project_id)})
    if project is None:
        raise Exception("Project not found")
    return project

def create_project(project: Project):
    res = projectCollection.insert_one(project)
    return res.inserted_id

def update_project(project_id: str, project: Project):
    res = projectCollection.update_one({"_id": ObjectId(project_id)}, {"$set": project})
    return res.acknowledged

def delete_project(project_id: str):
    res = projectCollection.delete_one({"_id": ObjectId(project_id)})
    return res.acknowledged


# task model crud functions
def get_task(task_id: str):
    task = taskCollection.find_one({"_id": ObjectId(task_id)})
    if task is None:
        raise Exception("Task not found")
    return task

def create_task(task: Task):
    res = taskCollection.insert_one(task)
    return res.inserted_id

def update_task(task_id: str, task: Task):
    res = taskCollection.update_one({"_id": ObjectId(task_id)}, {"$set": task})
    return res.acknowledged

def delete_task(task_id: str):
    res = taskCollection.delete_one({"_id": ObjectId(task_id)})
    return res.acknowledged



# issue model crud functions
def get_issue(issue_id: str):
    issue = issueCollection.find_one({"_id": ObjectId(issue_id)})
    if issue is None:
        raise Exception("Issue not found")
    return issue

def create_issue(issue: Issue):
    res = issueCollection.insert_one(issue)
    return res.inserted_id

def update_issue(issue_id: str, issue: Issue):
    res = issueCollection.update_one({"_id": ObjectId(issue_id)}, {"$set": issue})
    return res.acknowledged

def delete_issue(issue_id: str):
    res = issueCollection.delete_one({"_id": ObjectId(issue_id)})
    return res.acknowledged
