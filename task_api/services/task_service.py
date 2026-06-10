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