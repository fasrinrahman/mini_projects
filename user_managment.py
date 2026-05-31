# =========================
# MINI PROJECT 6
# User Management System
# =========================

import hashlib

FILE_NAME = "users.txt"


# -------------------------
# HASH PASSWORD
# -------------------------
def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# -------------------------
# REGISTER USER
# -------------------------
def register_user():

    username = input("Username: ")

    password = input("Password: ")

    role = input("Role (Admin/User): ")

    hashed_password = hash_password(password)

    with open(FILE_NAME, "a") as file:

        file.write(
            f"{username},{hashed_password},{role}\n"
        )

    print("User registered successfully")


# -------------------------
# LOGIN USER
# -------------------------
def login_user():

    username = input("Username: ")

    password = input("Password: ")

    hashed_password = hash_password(password)

    try:

        with open(FILE_NAME, "r") as file:

            for user in file:

                saved_username, saved_password, role = (
                    user.strip().split(",")
                )

                if (
                    username == saved_username
                    and hashed_password == saved_password
                ):

                    print(
                        f"Login Successful ({role})"
                    )

                    return

        print("Invalid credentials")

    except FileNotFoundError:

        print("No user database found")


# -------------------------
# VIEW USERS
# -------------------------
def view_users():

    try:

        with open(FILE_NAME, "r") as file:

            print("\nRegistered Users")

            for user in file:

                username, _, role = (
                    user.strip().split(",")
                )

                print(
                    f"Username: {username} | Role: {role}"
                )

    except FileNotFoundError:

        print("No user database found")


# -------------------------
# MENU
# -------------------------
def show_menu():

    print("\n===== USER MANAGEMENT =====")

    print("1. Register User")
    print("2. Login")
    print("3. View Users")
    print("4. Exit")


# -------------------------
# MAIN LOOP
# -------------------------
while True:

    show_menu()

    choice = input("Enter choice: ")

    if choice == "1":

        register_user()

    elif choice == "2":

        login_user()

    elif choice == "3":

        view_users()

    elif choice == "4":

        print("Exiting System")

        break

    else:

        print("Invalid choice")
        
        
        