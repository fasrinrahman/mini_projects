import sqlite3

DATABASE = "database.db"


def get_connection():

    return sqlite3.connect(DATABASE)


def initialize_database():

    connection = get_connection()

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
    
