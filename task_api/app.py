from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template

from database.db import initialize_database

from services.task_service import (
    get_all_tasks,
    get_task_by_id,
    create_task,
    update_task,
    delete_task
)

app = Flask(__name__)

initialize_database()


# -------------------------
# HOME
# -------------------------


@app.route("/api-info")
def home():

    return jsonify(
        {
            "project": "Task API",
            "version": "2.0",
            "status": "Running"
        }
    )

@app.route("/")
def index():

    return render_template("index.html")

# -------------------------
# GET ALL TASKS
# -------------------------

@app.route(
    "/tasks",
    methods=["GET"]
)
def get_tasks():

    return jsonify(
        {
            "success": True,
            "data": get_all_tasks()
        }
    )


# -------------------------
# GET TASK BY ID
# -------------------------

@app.route(
    "/tasks/<int:task_id>",
    methods=["GET"]
)
def get_task(task_id):

    task = get_task_by_id(task_id)

    if task:

        return jsonify(
            {
                "success": True,
                "data": task
            }
        )

    return jsonify(
        {
            "success": False,
            "message": "Task not found"
        }
    ), 404


# -------------------------
# CREATE TASK
# -------------------------

@app.route(
    "/tasks",
    methods=["POST"]
)
def add_task():

    data = request.json

    if not data.get("title"):

        return jsonify(
            {
                "success": False,
                "message": "Title is required"
            }
        ), 400

    create_task(
        data["title"],
        data.get(
            "status",
            "Pending"
        )
    )

    return jsonify(
        {
            "success": True,
            "message": "Task created"
        }
    )


# -------------------------
# UPDATE TASK
# -------------------------

@app.route(
    "/tasks/<int:task_id>",
    methods=["PUT"]
)
def edit_task(task_id):

    data = request.json

    update_task(
        task_id,
        data["title"],
        data["status"]
    )

    return jsonify(
        {
            "success": True,
            "message": "Task updated"
        }
    )


# -------------------------
# DELETE TASK
# -------------------------

@app.route(
    "/tasks/<int:task_id>",
    methods=["DELETE"]
)
def remove_task(task_id):

    delete_task(task_id)

    return jsonify(
        {
            "success": True,
            "message": "Task deleted"
        }
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )