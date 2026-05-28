# =========================
# MINI PROJECT 3
# Student Management System
# =========================

print("=== STUDENT MANAGEMENT SYSTEM ===")

FILE_NAME = "students.txt"


# -------------------------
# ADD STUDENT
# -------------------------
def add_student():

    name = input("Enter student name: ")

    marks = input("Enter student marks: ")

    with open(FILE_NAME, "a") as file:

        file.write(f"{name},{marks}\n")

    print("Student added successfully")


# -------------------------
# VIEW STUDENTS
# -------------------------
def view_students():

    try:

        with open(FILE_NAME, "r") as file:

            students = file.readlines()

            if not students:

                print("No student records found")

                return

            print("\nStudent Records:")

            for index, student in enumerate(students):

                name, marks = student.strip().split(",")

                print(
                    f"{index + 1}. Name: {name} | Marks: {marks}"
                )

    except FileNotFoundError:

        print("No records file found")


# -------------------------
# SEARCH STUDENT
# -------------------------
def search_student():

    search_name = input(
        "Enter student name to search: "
    )

    found = False

    try:

        with open(FILE_NAME, "r") as file:

            for student in file:

                name, marks = student.strip().split(",")

                if name.lower() == search_name.lower():

                    print(
                        f"Found -> Name: {name}, Marks: {marks}"
                    )

                    found = True

                    break

        if not found:

            print("Student not found")

    except FileNotFoundError:

        print("No records file found")


# -------------------------
# DELETE STUDENT
# -------------------------
def delete_student():

    delete_name = input(
        "Enter student name to delete: "
    )

    updated_students = []

    found = False

    try:

        with open(FILE_NAME, "r") as file:

            students = file.readlines()

        for student in students:

            name, marks = student.strip().split(",")

            if name.lower() != delete_name.lower():

                updated_students.append(student)

            else:

                found = True

        with open(FILE_NAME, "w") as file:

            file.writelines(updated_students)

        if found:

            print("Student deleted successfully")

        else:

            print("Student not found")

    except FileNotFoundError:

        print("No records file found")


# -------------------------
# MENU
# -------------------------
def show_menu():

    print("\nChoose Option")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")


# -------------------------
# MAIN LOOP
# -------------------------
while True:

    show_menu()

    choice = input("Enter choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        delete_student()

    elif choice == "5":

        print("Exiting System")

        break

    else:

        print("Invalid choice")