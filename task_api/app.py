from flask import Flask
from flask import jsonify
from flask import request

from database.db import initialize_database

from services.task_service import (
    get_all_tasks,
    create_task,
    delete_task
)

app = Flask(__name__)

initialize_database()


# -------------------------
# GET ALL TASKS
# -------------------------
@app.route(
    "/tasks",
    methods=["GET"]
)
def get_tasks():

    return jsonify(
        get_all_tasks()
    )


# -------------------------
# CREATE TASK
# -------------------------
@app.route(
    "/tasks",
    methods=["POST"]
)
def add_task():

    data = request.json

    create_task(
        data["title"],
        data["status"]
    )

    return jsonify(
        {"message": "Task Created"}
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
        {"message": "Task Deleted"}
    )


if __name__ == "__main__":

    app.run(debug=True)

