from database.db import get_connection

def create_task(data, user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks
        (title, description, status, priority, due_date, user_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["title"],
        data.get("description", ""),
        data.get("status", "Todo"),
        data.get("priority", "Low"),
        data.get("due_date", ""),
        user_id
    ))

    conn.commit()
    conn.close()


def get_tasks(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tasks WHERE user_id = ?
    """, (user_id,))

    tasks = cursor.fetchall()
    conn.close()

    return tasks
