from flask import Flask
from flask import request
from flask import jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"


def initialize_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT NOT NULL,

        status TEXT NOT NULL
    )
    """)

    connection.commit()

    connection.close()


initialize_database()

@app.route("/tasks", methods=["GET"])
def get_tasks():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM tasks"
    )

    tasks = cursor.fetchall()

    connection.close()

    result = []

    for task in tasks:

        result.append({
            "id": task[0],
            "title": task[1],
            "status": task[2]
        })

    return jsonify(result)

@app.route("/tasks", methods=["POST"])
def create_task():

    data = request.json

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tasks
        (title, status)
        VALUES (?, ?)
        """,
        (
            data["title"],
            data["status"]
        )
    )

    connection.commit()

    connection.close()

    return jsonify(
        {"message": "Task Created"}
    )
    
@app.route(
    "/tasks/<int:task_id>",
    methods=["DELETE"]
)
def delete_task(task_id):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM tasks
        WHERE id = ?
        """,
        (task_id,)
    )

    connection.commit()

    connection.close()

    return jsonify(
        {"message": "Task Deleted"}
    )
    
if __name__ == "__main__":

    app.run(debug=True)