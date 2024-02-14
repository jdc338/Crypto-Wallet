from werkzeug.security import generate_password_hash, check_password_hash
from app.database import get_db
from flask import session

def login_user(username, password):
    try:
        db = get_db()
        user = db.users.find_one({"username": username})
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = str(user['_id'])  # Example for session-based auth
            return True
        else:
            return "Invalid username or password."
    except Exception as e:
        # Log the exception for debugging
        print(f"An error occurred: {e}")
        return "An error occurred during login."

def logout_user():
    session.pop('user_id', None)  # Example for session-based auth
    # Handle token invalidation if using token-based auth
    return True

def hash_password(password):
    return generate_password_hash(password)

def check_password(hashed_password, password):
    return check_password_hash(hashed_password, password)
