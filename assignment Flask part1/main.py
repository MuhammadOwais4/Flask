from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="signup_login"
)

cursor = db.cursor()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if 'name' in data and 'email' in data and 'password' in data and 'dob' in data and 'phone' in data:
        name = data['name']
        email = data['email']
        password = data['password']
        dob = data['dob']
        phone = data['phone']
        cursor.execute("INSERT INTO user (name, email, password, dob, phone) VALUES (%s, %s, %s, %s, %s)",
                       (name, email, password, dob, phone))
        db.commit()
        return jsonify({'message': 'User added successfully'}), 201

    return jsonify({'message': 'Missing required data'}), 400

@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT id, name, email, dob, phone, created_at FROM signup_login")
    users = cursor.fetchall()
    user_list = []
    for user in users:
        user_data = {
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'dob': user[3].strftime('%Y-%m-%d'),
            'phone': user[4],
            'created_at': user[5].strftime('%Y-%m-%d %H:%M:%S')
        }
        user_list.append(user_data)
    return jsonify(user_list)

@app.route('/change-password', methods=['PATCH'])
def change_password():
    data = request.get_json()
    if 'id' in data and 'password' in data:
        user_id = data['id']
        new_password = data['password']
        cursor.execute("UPDATE signup_login SET password = %s WHERE id = %s", (new_password, user_id))
        db.commit()
        return jsonify({'message': 'Password updated successfully'}), 200

    return jsonify({'message': 'Missing user ID or new password'}), 400

# API for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'email' in data and 'password' in data:
        email = data['email']
        password = data['password']
        cursor.execute("SELECT id FROM signup_login WHERE email = %s AND password = %s", (email, password))
        user_id = cursor.fetchone()
        if user_id:
            return jsonify({'message': 'User login successfully'}), 200

        return jsonify({'message': 'User login failed: invalid email or password'}), 401

    return jsonify({'message': 'Missing email or password'}), 400

if __name__ == '__main__':
    app.run(debug=True)
