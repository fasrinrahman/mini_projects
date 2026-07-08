# import sqlite3

# DATABASE_NAME = "taskflow.db"


# def get_connection():
#     """
#     Create and return a database connection.
#     """

#     connection = sqlite3.connect(DATABASE_NAME)

#     # Allow accessing columns by name
#     connection.row_factory = sqlite3.Row

#     return connection


# def initialize_database():
#     """
#     Create the tasks table if it does not exist.
#     """

#     connection = get_connection()

#     cursor = connection.cursor()

#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS tasks (

#             id INTEGER PRIMARY KEY AUTOINCREMENT,

#             title TEXT NOT NULL,

#             description TEXT,

#             status TEXT NOT NULL DEFAULT 'Todo',

#             priority TEXT NOT NULL DEFAULT 'Medium',

#             category TEXT,

#             due_date TEXT,

#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

#             updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

#         );
#         """
#     )

#     connection.commit()

#     connection.close()

import sqlite3

DATABASE = "taskflow_saas.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # TASKS TABLE (SAAS VERSION)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT,
            priority TEXT,
            due_date TEXT,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()
    