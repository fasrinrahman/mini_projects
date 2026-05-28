# =========================
# MINI PROJECT 2
# Todo App
# =========================

print("=== TODO APPLICATION ===")

tasks = []


# -------------------------
# SHOW MENU
# -------------------------
def show_menu():

    print("\nChoose Option")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")


# -------------------------
# ADD TASK
# -------------------------
def add_task():

    task = input("Enter task: ")

    tasks.append(task)

    print("Task added successfully")


# -------------------------
# VIEW TASKS
# -------------------------
def view_tasks():

    if not tasks:

        print("No tasks available")

        return

    print("\nTasks List:")

    for index, task in enumerate(tasks):

        print(f"{index + 1}. {task}")


# -------------------------
# UPDATE TASK
# -------------------------
def update_task():

    view_tasks()

    if not tasks:
        return

    task_number = int(
        input("Enter task number to update: ")
    )

    if 1 <= task_number <= len(tasks):

        new_task = input("Enter new task: ")

        tasks[task_number - 1] = new_task

        print("Task updated successfully")

    else:

        print("Invalid task number")


# -------------------------
# DELETE TASK
# -------------------------
def delete_task():

    view_tasks()

    if not tasks:
        return

    task_number = int(
        input("Enter task number to delete: ")
    )

    if 1 <= task_number <= len(tasks):

        removed_task = tasks.pop(task_number - 1)

        print(f"Deleted: {removed_task}")

    else:

        print("Invalid task number")


# -------------------------
# MAIN LOOP
# -------------------------
while True:

    show_menu()

    choice = input("Enter choice: ")

    if choice == "1":

        add_task()

    elif choice == "2":

        view_tasks()

    elif choice == "3":

        update_task()

    elif choice == "4":

        delete_task()

    elif choice == "5":

        print("Exiting Todo App")

        break

    else:

        print("Invalid choice")
        