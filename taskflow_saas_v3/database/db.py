import sqlite3

DATABASE = "database.db"


def get_connection():

    connection = sqlite3.connect(
        DATABASE
    )

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            description TEXT,

            priority TEXT,

            status TEXT,

            due_date TEXT,

            created_at TEXT
        )
        """
    )

    connection.commit()

    connection.close()