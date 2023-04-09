from pymongo import MongoClient
from api.model.Model import User, Project, Task, Issue
from bson import ObjectId
from dotenv import load_dotenv
import os
from datetime import datetime

now = datetime.now()
config = load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

try:
    client = MongoClient(
        "mongodb+srv://%s:%s@cluster0.yumdxcu.mongodb.net/?retryWrites=true&w=majority" % (USERNAME, PASSWORD))
    print("Connected to MongoDB")
except Exception as e:
    print(e)

db = client.projectCollaboration
projectCollection = db.projects
taskCollection = db.tasks
issueCollection = db.issues
userCollection = db.users

# user model crud functions


def get_user(user_id: str):
    user = userCollection.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise Exception("User not found")
    return user


def create_user(user: User):
    user = User(name=user["name"], skills=user["skills"], email=user["email"])
    res = userCollection.insert_one(user)
    return res.inserted_id


def update_user(user_id: str, user: User):
    user = User(name=user["name"], skills=user["skills"], email=user["email"])
    res = userCollection.update_one({"_id": ObjectId(user_id)}, {"$set": user})
    return res.acknowledged


def delete_user(user_id: str):
    res = userCollection.delete_one({"_id": ObjectId(user_id)})
    return res.acknowledged


def get_paginated_users(page: int, limit: int):
    users = userCollection.find().skip((page - 1) * limit).limit(limit)
    return users


# project model crud functions
def get_project(project_id: str):
    project = projectCollection.find_one({"_id": ObjectId(project_id)})
    if project is None:
        raise Exception("Project not found")
    return project


def create_project(project: Project):
    project = Project(name=project["name"], description=project["description"],
                      status=project["status"], created_at=now, updated_at=now)
    res = projectCollection.insert_one(project)
    return res.inserted_id


def update_project(project_id: str, project: Project):
    project = Project(name=project["name"], description=project["description"],
                      status=project["status"], updated_at=now)
    res = projectCollection.update_one(
        {"_id": ObjectId(project_id)}, {"$set": project})
    return res.acknowledged


def delete_project(project_id: str):
    res = projectCollection.delete_one({"_id": ObjectId(project_id)})
    return res.acknowledged


def get_paginated_projects(page: int, limit: int):
    sort_order = [("created_at", -1)]
    projects = projectCollection.find().sort(
        sort_order).skip((page - 1) * limit).limit(limit)
    return projects


# task model crud functions
def get_task(task_id: str):
    task = taskCollection.find_one({"_id": ObjectId(task_id)})
    if task is None:
        raise Exception("Task not found")
    return task


def create_task(task: Task):
    task = Task(project_id_ref=ObjectId(task["project_id_ref"]), name=task["name"], description=task["description"],
                status=task["status"], user_ids=task["user_ids"], created_at=now, updated_at=now)
    res = taskCollection.insert_one(task)
    return res.inserted_id


def update_task(task_id: str, task: Task):
    task = Task(project_id_ref=ObjectId(task["project_id_ref"]), name=task["name"], description=task["description"],
                status=task["status"], user_ids=task["user_ids"], updated_at=now)
    res = taskCollection.update_one({"_id": ObjectId(task_id)}, {"$set": task})
    return res.acknowledged


def delete_task(task_id: str):
    res = taskCollection.delete_one({"_id": ObjectId(task_id)})
    return res.acknowledged


def get_paginated_tasks(page: int, limit: int):
    sort_order = [("created_at", -1)]
    tasks = taskCollection.find().sort(sort_order).skip(
        (page - 1) * limit).limit(limit)
    return tasks


def get_tasks_by_project_id(project_id: str):
    tasks = taskCollection.find({"project_id_ref": ObjectId(project_id)})
    return tasks


# issue model crud functions
def get_issue(issue_id: str):
    issue = issueCollection.find_one({"_id": ObjectId(issue_id)})
    if issue is None:
        raise Exception("Issue not found")
    return issue


def create_issue(issue: Issue):
    issue = Issue(task_id_ref=ObjectId(issue["task_id_ref"]), issue_tag=issue["issue_tag"], status=issue["status"],
                  priority=issue["priority"], user_id=ObjectId(issue["user_id"]), created_at=now, updated_at=now)
    res = issueCollection.insert_one(issue)
    return res.inserted_id


def update_issue(issue_id: str, issue: Issue):
    issue = Issue(task_id_ref=ObjectId(issue["task_id_ref"]), issue_tag=issue["issue_tag"], status=issue["status"],
                  priority=issue["priority"], user_id=ObjectId(issue["user_id"]), updated_at=now)
    res = issueCollection.update_one(
        {"_id": ObjectId(issue_id)}, {"$set": issue})
    return res.acknowledged


def delete_issue(issue_id: str):
    res = issueCollection.delete_one({"_id": ObjectId(issue_id)})
    return res.acknowledged


def get_paginated_issues(page: int, limit: int):
    sort_order = [("created_at", -1)]
    issues = issueCollection.find().sort(
        sort_order).skip((page - 1) * limit).limit(limit)
    return issues


def get_issues_by_task_id(task_id: str):
    issues = issueCollection.find({"task_id_ref": ObjectId(task_id)})
    return issues


def get_project_completion_percentage(project_id):
    tasks = get_tasks_by_project_id(project_id)
    completed_tasks = tasks.filter(status='completed')
    return completed_tasks.count() / tasks.count()
