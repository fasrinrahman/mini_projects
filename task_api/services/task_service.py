from database.db import get_connection


# -------------------------
# GET ALL TASKS
# -------------------------

def get_all_tasks():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM tasks"
    )

    rows = cursor.fetchall()

    connection.close()

    tasks = []

    for row in rows:

        tasks.append(
            {
                "id": row[0],
                "title": row[1],
                "status": row[2]
            }
        )

    return tasks

# -------------------------
# SEARCH TASKS
# -------------------------

def search_tasks(keyword):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE title LIKE ?
        """,
        (f"%{keyword}%",)
    )

    rows = cursor.fetchall()

    connection.close()

    tasks = []

    for row in rows:

        tasks.append(
            {
                "id": row[0],
                "title": row[1],
                "status": row[2]
            }
        )

    return tasks

# -------------------------
# FILTER TASKS BY STATUS    
# -------------------------

def filter_tasks(status):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE status = ?
        """,
        (status,)
    )

    rows = cursor.fetchall()

    connection.close()

    tasks = []

    for row in rows:

        tasks.append(
            {
                "id": row[0],
                "title": row[1],
                "status": row[2]
            }
        )

    return tasks

# -------------------------------
#  Filter task by filter and call
# -------------------------------
def get_statistics():

    tasks = get_all_tasks()

    total = len(tasks)

    completed = len(
        [
            task
            for task in tasks
            if task["status"] == "Completed"
        ]
    )

    pending = total - completed

    completion_rate = 0

    if total > 0:

        completion_rate = round(
            (completed / total) * 100,
            2
        )

    return {

        "total": total,

        "completed": completed,

        "pending": pending,

        "completion_rate":
            completion_rate
    }


# -------------------------
# GET TASK BY ID
# -------------------------

def get_task_by_id(task_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE id = ?
        """,
        (task_id,)
    )

    row = cursor.fetchone()

    connection.close()

    if row:

        return {
            "id": row[0],
            "title": row[1],
            "status": row[2]
        }

    return None


# -------------------------
# CREATE TASK
# -------------------------

def create_task(title, status):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tasks
        (title, status)
        VALUES (?, ?)
        """,
        (title, status)
    )

    connection.commit()

    connection.close()


# -------------------------
# UPDATE TASK
# -------------------------

def update_task(
    task_id,
    title,
    status
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET title = ?, status = ?
        WHERE id = ?
        """,
        (
            title,
            status,
            task_id
        )
    )

    connection.commit()

    connection.close()


# -------------------------
# DELETE TASK
# -------------------------

def delete_task(task_id):

    connection = get_connection()

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