from flask import Flask, jsonify, request, render_template
from database.db import initialize_database
from services.task_service import (
    get_all_tasks,
    create_task,
    delete_task,
    update_task,
    search_tasks,
    filter_tasks,
    get_statistics
)

app = Flask(__name__)

initialize_database()

@app.route("/")
def home():
    return render_template("index.html")


# =====================
# TASKS API
# =====================

@app.route("/tasks", methods=["GET"])
def tasks():
    return jsonify({
        "success": True,
        "data": get_all_tasks()
    })


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json

    if not data.get("title"):
        return jsonify({"success": False, "message": "Title required"}), 400

    create_task(
        data["title"],
        data.get("status", "Pending"),
        data.get("priority", "Medium"),
        data.get("due_date", None)
    )

    return jsonify({"success": True, "message": "Task created"})


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    delete_task(task_id)
    return jsonify({"success": True})


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    data = request.json
    update_task(task_id, data)
    return jsonify({"success": True})


@app.route("/tasks/search")
def search():
    q = request.args.get("q", "")
    return jsonify({"success": True, "data": search_tasks(q)})


@app.route("/tasks/filter")
def filter_api():
    status = request.args.get("status")
    priority = request.args.get("priority")
    return jsonify({"success": True, "data": filter_tasks(status, priority)})


@app.route("/tasks/stats")
def stats():
    return jsonify({"success": True, "data": get_statistics()})


if __name__ == "__main__":
    app.run(debug=True)