from models.user_model import create_user, get_user

def register_user(username, password):
    return create_user(username, password)


def login_user(username, password):
    user = get_user(username)

    if user and user[2] == password:
        return {
            "id": user[0],
            "username": user[1]
        }

    return None