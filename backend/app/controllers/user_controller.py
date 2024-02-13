# Some controller or route file
from app.database import get_db

db = get_db()
# Use the db object to interact with your MongoDB collections


def add_user(username, email, password_hash):
    user = {
        "username": username,
        "email": email,
        "password_hash": password_hash,
        "wallets": []
    }
    return db.users.insert_one(user).inserted_id


def get_user(username):
    return db.users.find_one({"username": username})


def update_user_email(username, new_email):
    result = db.users.update_one({"username": username}, {"$set": {"email": new_email}})
    return result.modified_count  # Returns the number of documents modified

def delete_user(username):
    result = db.users.delete_one({"username": username})
    return result.deleted_count  # Returns the number of documents deleted
