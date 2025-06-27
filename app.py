from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary data store
users = {
    "1": {"id": 1, "name": "Abhijeet", "email": "abhijeet@example.com"},
    "2": {"id": 2, "name": "Sarthak", "email": "sarthak@example.com"}
}

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Add new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = str(data.get('id'))

    if user_id in users:
        return jsonify({"error": "User already exists"}), 409

    users[user_id] = data
    return jsonify({"message": "User added"}), 201

# Update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    users[user_id].update(request.json)
    return jsonify({"message": "User updated"})

# Delete user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted"})

# Home route
@app.route('/')
def home():
    return "✅ Flask API is running!"

# Start the app
if __name__ == '__main__':
    app.run(debug=True)