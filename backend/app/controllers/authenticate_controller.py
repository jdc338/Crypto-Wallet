from werkzeug.security import generate_password_hash, check_password_hash
from app.database import get_db
from flask import session
import pyotp

def login_user(username, password):
    try:
        db = get_db()
        user = db.users.find_one({"username": username})
        if user and check_password_hash(user['password_hash'], password):
            # Check if 2FA is enabled for the user
            if '2fa_secret' in user:
                # User must verify 2FA token
                session['2fa_user_id'] = str(user['_id'])  # Temporarily store user ID for 2FA verification
                return "2FA verification required"
            else:
                # If 2FA is not enabled, proceed to log in the user
                session['user_id'] = str(user['_id'])
                return "Logged in successfully"
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
