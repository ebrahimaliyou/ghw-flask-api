from api.service import Service
from bson import json_util
from flask import Blueprint, request
from flask_cors import CORS
from datetime import datetime

routes = Blueprint("api", __name__)
CORS(routes)

now = datetime.now()


@routes.route("/users", methods=["GET", "POST", "PUT", "DELETE"], defaults={"id": None})
@routes.route("/users/<id>")
def user(id):
    user_id = id
    if request.method == "GET":
        if user_id is None:
            page = int(request.args.get("page", 1))
            limit = int(request.args.get("limit", 10))
            users = Service.get_paginated_users(page, limit)
            return json_util.dumps(users)
        user = Service.get_user(user_id)
        return json_util.dumps(user)
    elif request.method == "POST":
        user = request.get_json()
        res = Service.create_user(user)
        return json_util.dumps(res)
    elif request.method == "PUT":
        user = request.get_json()
        res = Service.update_user(user_id, user)
        return json_util.dumps(res)
    elif request.method == "DELETE":
        res = Service.delete_user(user_id)
        return json_util.dumps(res)


@routes.route("/projects/", methods=["GET", "POST", "PUT", "DELETE"], defaults={"id": None})
@routes.route("/projects/<id>")
def project(id):
    project_id = id
    if request.method == "GET":
        if project_id is None:
            page = int(request.args.get("page", 1))
            limit = int(request.args.get("limit", 10))
            projects = Service.get_paginated_projects(page, limit)
            return json_util.dumps(projects)
        project = Service.get_project(project_id)
        return json_util.dumps(project)
    elif request.method == "POST":
        project = request.get_json()
        res = Service.create_project(project)
        return json_util.dumps(res)
    elif request.method == "PUT":
        project_id = request.args.get("id")
        if project_id is None:
            raise Exception("Project id is required")
        project = request.get_json()
        res = Service.update_project(project_id, project)
        return json_util.dumps(res)
    elif request.method == "DELETE":
        project_id = request.args.get("id")
        if project_id is None:
            raise Exception("Project id is required")
        res = Service.delete_project(project_id)
        return json_util.dumps(res)


@routes.route("/tasks/<id>", methods=["GET", "POST", "PUT", "DELETE"], defaults={"id": None})
@routes.route("/tasks/<id>")
def task(id):
    task_id = id
    if request.method == "GET":
        if task_id is None:
            page = int(request.args.get("page", 1))
            limit = int(request.args.get("limit", 10))
            tasks = Service.get_paginated_tasks(page, limit)
            return json_util.dumps(tasks)
        if request.args.get("project_id"):
            project_id = request.args.get("project_id")
            tasks = Service.get_tasks_by_project_id(project_id)
            return json_util.dumps(tasks)
        task = Service.get_task(task_id)
        return json_util.dumps(task)
    elif request.method == "POST":
        task = request.get_json()
        res = Service.create_task(task)
        return json_util.dumps(res)
    elif request.method == "PUT":
        task_id = request.args.get("id")
        if task_id is None:
            raise Exception("Task id is required")
        task = request.get_json()
        res = Service.update_task(task_id, task)
        return json_util.dumps(res)
    elif request.method == "DELETE":
        task_id = request.args.get("id")
        if task_id is None:
            raise Exception("Task id is required")
        res = Service.delete_task(task_id)
        return json_util.dumps(res)


@routes.route("/issues/<id>", methods=["GET", "POST", "PUT", "DELETE"], defaults={"id": None})
@routes.route("/issues/<id>")
def issue(id):
    issue_id = id
    if request.method == "GET":
        if issue_id is None:
            page = int(request.args.get("page", 1))
            limit = int(request.args.get("limit", 10))
            issues = Service.get_paginated_issues(page, limit)
            return json_util.dumps(issues)
        if request.args.get("task_id"):
            task_id = request.args.get("task_id")
            issues = Service.get_issues_by_task_id(task_id)
            return json_util.dumps(issues)
        issue = Service.get_issue(issue_id)
        return json_util.dumps(issue)
    elif request.method == "POST":
        issue = request.get_json()
        res = Service.create_issue(issue)
        return json_util.dumps(res)
    elif request.method == "PUT":
        issue_id = request.args.get("id")
        if issue_id is None:
            raise Exception("Issue id is required")
        issue = request.get_json()
        res = Service.update_issue(issue_id, issue)
        return json_util.dumps(res)
    elif request.method == "DELETE":
        issue_id = request.args.get("id")
        if id is None:
            raise Exception("Issue id is required")
        res = Service.delete_issue(issue_id)
        return json_util.dumps(res)


@routes.route("/projectCompletion/<id>", methods=["GET"], defaults={"id": None})
@routes.route("/projectCompletion/<id>")
def projectCompletion(id):
    project_id = id
    if project_id is None:
        raise Exception("Project ID is required")
    projectCompletionPercentage = Service.get_project_completion_percentage(
        project_id)
    return json_util.dumps(projectCompletionPercentage)
