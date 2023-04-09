from api.service import Service
from api.model.Model import User, Project, Task, Issue
from bson import ObjectId, json_util
from flask import Blueprint, request
from flask_cors import CORS
from datetime import datetime

routes = Blueprint("api", __name__)
CORS(routes)

now = datetime.now()

@routes.route("/user", methods=["GET", "POST", "PUT", "DELETE"])
def user():
    if request.method == "GET":
        user_id = request.args.get("id")
        user = Service.get_user(user_id)
        return json_util.dumps(user)
    elif request.method == "POST":
        user = request.get_json()
        user = User(name=user["name"], skills=user["skills"], email=user["email"])
        res = Service.create_user(user)
        return json_util.dumps(res)
    elif request.method == "PUT":
        user_id = request.args.get("id")
        user = request.get_json()
        user = User(name=user["name"], skills=user["skills"], email=user["email"])
        res = Service.update_user(user_id, user)
        return json_util.dumps(res)
    elif request.method == "DELETE":
        user_id = request.args.get("id")
        res = Service.delete_user(user_id)
        return json_util.dumps(res)
    
@routes.route("/project", methods=["GET", "POST", "PUT", "DELETE"])
def project():
    if request.method == "GET":
        project_id = request.args.get("id")
        project = Service.get_project(project_id)
        return json_util.dumps(project)
    elif request.method == "POST":
        project = request.get_json()
        project = Project(name=project["name"], description=project["description"], status=project["status"], created_at=now, updated_at=now)
        res = Service.create_project(project)
        return json_util.dumps(res)
    elif request.method == "PUT":
        project_id = request.args.get("id")
        project = request.get_json()
        project = Project(name=project["name"], description=project["description"], status=project["status"], created_at=now, updated_at=now)
        res = Service.update_project(project_id, project)
        return json_util.dumps(res)
    elif request.method == "DELETE":
        project_id = request.args.get("id")
        res = Service.delete_project(project_id)
        return json_util.dumps(res)
    
@routes.route("/task", methods=["GET", "POST", "PUT", "DELETE"])
def task():
    if request.method == "GET":
        task_id = request.args.get("id")
        task = Service.get_task(task_id)
        return json_util.dumps(task)
    elif request.method == "POST":
        task = request.get_json()
        task = Task(project_id_ref=ObjectId(task["project_id_ref"]), name=task["name"], description=task["description"], status=task["status"], user_ids=task["user_ids"], created_at=now, updated_at=now)
        res = Service.create_task(task)
        return json_util.dumps(res)
    elif request.method == "PUT":
        task_id = request.args.get("id")
        task = request.get_json()
        task = Task(project_id_ref=ObjectId(task["project_id_ref"]), name=task["name"], description=task["description"], status=task["status"], user_ids=task["user_ids"], created_at=now, updated_at=now)
        res = Service.update_task(task_id, task)
        return json_util.dumps(res)
    elif request.method == "DELETE":
        task_id = request.args.get("id")
        res = Service.delete_task(task_id)
        return json_util.dumps(res)
    
@routes.route("/issue", methods=["GET", "POST", "PUT", "DELETE"])
def issue():
    if request.method == "GET":
        issue_id = request.args.get("id")
        issue = Service.get_issue(issue_id)
        return json_util.dumps(issue)
    elif request.method == "POST":
        issue = request.get_json()
        issue = Issue(task_id_ref=ObjectId(issue["task_id_ref"]), issue_tag=issue["issue_tag"], status=issue["status"], priority=issue["priority"], user_id=ObjectId(issue["user_id"]), created_at=now, updated_at=now)
        res = Service.create_issue(issue)
        return json_util.dumps(res)
    elif request.method == "PUT":
        issue_id = request.args.get("id")
        issue = request.get_json()
        issue = Issue(task_id_ref=ObjectId(issue["task_id_ref"]), issue_tag=issue["issue_tag"], status=issue["status"], priority=issue["priority"], user_id=ObjectId(issue["user_id"]), created_at=now, updated_at=now)
        res = Service.update_issue(issue_id, issue)
        return json_util.dumps(res)
    elif request.method == "DELETE":
        issue_id = request.args.get("id")
        res = Service.delete_issue(issue_id)
        return json_util.dumps(res)

