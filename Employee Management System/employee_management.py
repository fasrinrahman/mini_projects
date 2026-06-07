# =========================
# MINI PROJECT 8
# Employee Management System
# =========================

import sqlite3

DATABASE = "emp_managment.db"


# -------------------------
# CREATE DATABASE TABLE
# -------------------------
def create_table():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        department TEXT NOT NULL,

        salary REAL NOT NULL
    )
    """)

    connection.commit()

    connection.close()


# -------------------------
# ADD EMPLOYEE
# -------------------------
def add_employee():

    name = input("Employee Name: ")

    department = input("Department: ")

    salary = float(input("Salary: "))

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO employees
        (name, department, salary)
        VALUES (?, ?, ?)
        """,
        (name, department, salary)
    )

    connection.commit()

    connection.close()

    print("Employee added successfully")


# -------------------------
# VIEW EMPLOYEES
# -------------------------
def view_employees():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM employees"
    )

    employees = cursor.fetchall()

    connection.close()

    if not employees:

        print("No employee records found")

        return

    print("\nEmployee List")

    for employee in employees:

        print(employee)


# -------------------------
# SEARCH EMPLOYEE
# -------------------------
def search_employee():

    employee_id = input(
        "Employee ID: "
    )

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM employees
        WHERE id = ?
        """,
        (employee_id,)
    )

    employee = cursor.fetchone()

    connection.close()

    if employee:

        print(employee)

    else:

        print("Employee not found")


# -------------------------
# DELETE EMPLOYEE
# -------------------------
def delete_employee():

    employee_id = input(
        "Employee ID: "
    )

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM employees
        WHERE id = ?
        """,
        (employee_id,)
    )

    connection.commit()

    connection.close()

    print("Employee deleted successfully")


# -------------------------
# MENU
# -------------------------
def show_menu():

    print("\n===== EMPLOYEE SYSTEM =====")

    print("1. Add Employee")

    print("2. View Employees")

    print("3. Search Employee")

    print("4. Delete Employee")

    print("5. Exit")


# -------------------------
# MAIN PROGRAM
# -------------------------
create_table()

while True:

    show_menu()

    choice = input("Choice: ")

    if choice == "1":

        add_employee()

    elif choice == "2":

        view_employees()

    elif choice == "3":

        search_employee()

    elif choice == "4":

        delete_employee()

    elif choice == "5":

        print("Goodbye")

        break

    else:

        print("Invalid choice")