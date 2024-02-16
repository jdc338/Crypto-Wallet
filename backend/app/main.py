from flask import Flask, request, jsonify
from app.controllers.user_controller import add_user

app = Flask(__name__)

@app.route('/create_account', methods=['POST'])
def create_account():
    user_data = request.json
    username = user_data.get('username')
    email = user_data.get('email')
    password = user_data.get('password')
    user_id = add_user(username, email, password)  # Assumes password hashing within add_user
    if user_id:
        return jsonify({"message": "Account created successfully", "user_id": str(user_id)}), 201
    else:
        return jsonify({"error": "Account creation failed"}), 400

if __name__ == '__main__':
    app.run(debug=True)
