from database.db import get_connection

# =========================
# GET ALL TASKS
# =========================
def get_all_tasks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


# =========================
# GET TASK BY ID
# =========================
def get_task_by_id(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None


# =========================
# CREATE TASK
# =========================
def create_task(title, description="", status="Todo", priority="Medium"):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, description, status, priority)
        VALUES (?, ?, ?, ?)
        """,
        (title, description, status, priority)
    )

    conn.commit()
    conn.close()


# =========================
# UPDATE TASK
# =========================
def update_task(task_id, title, description, status, priority):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET title = ?,
            description = ?,
            status = ?,
            priority = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (title, description, status, priority, task_id)
    )

    conn.commit()
    conn.close()


# =========================
# DELETE TASK
# =========================
def delete_task(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()


# =========================
# GET STATS (for dashboard later)
# =========================
def get_task_stats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT status, COUNT(*) as count FROM tasks GROUP BY status")
    rows = cursor.fetchall()

    conn.close()

    return {row["status"]: row["count"] for row in rows}

from database.db import get_connection

def row_to_dict(row):
    return {
        "id": row[0],
        "title": row[1],
        "status": row[2],
        "priority": row[3],
        "due_date": row[4]
    }


def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [row_to_dict(r) for r in rows]


def create_task(title, status, priority, due_date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, status, priority, due_date)
        VALUES (?, ?, ?, ?)
    """, (title, status, priority, due_date))

    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


def update_task(task_id, data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET title=?, status=?, priority=?, due_date=?
        WHERE id=?
    """, (
        data.get("title"),
        data.get("status"),
        data.get("priority"),
        data.get("due_date"),
        task_id
    ))

    conn.commit()
    conn.close()


def search_tasks(keyword):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tasks
        WHERE title LIKE ?
        ORDER BY id DESC
    """, (f"%{keyword}%",))

    rows = cursor.fetchall()
    conn.close()

    return [row_to_dict(r) for r in rows]


def filter_tasks(status, priority):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM tasks WHERE 1=1"
    params = []

    if status:
        query += " AND status=?"
        params.append(status)

    if priority:
        query += " AND priority=?"
        params.append(priority)

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    return [row_to_dict(r) for r in rows]


def get_statistics():
    tasks = get_all_tasks()

    total = len(tasks)
    completed = len([t for t in tasks if t["status"] == "Completed"])
    pending = total - completed

    return {
        "total": total,
        "completed": completed,
        "pending": pending
    }
