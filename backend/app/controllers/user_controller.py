# Some controller or route file
from app.database import get_db
from pymongo.errors import DuplicateKeyError

db = get_db()
# Use the db object to interact with your MongoDB collections

def add_user(username, email, password_hash):
    try:
        user = {
            "username": username,
            "email": email,
            "password_hash": password_hash,
            "wallets": []
        }
        return db.users.insert_one(user).inserted_id
    except DuplicateKeyError:
        # Handle the error when a duplicate username or email is encountered
        return None
    except Exception as e:
        # Handle any other database errors
        print(f"An error occurred: {e}")
        return None


def get_user(username):
    user = db.users.find_one({"username": username})
    if user is not None:
        return user
    else:
        # Handle the situation where the user is not found
        print("User not found.")
        return None


def update_user_email(username, new_email):
    try:
        result = db.users.update_one({"username": username}, {"$set": {"email": new_email}})
        if result.modified_count == 0:
            # No document was modified, indicating the user was not found
            return False
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def delete_user(username):
    try:
        result = db.users.delete_one({"username": username})
        if result.deleted_count == 0:
            # No document was deleted, indicating the user was not found
            return False
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
