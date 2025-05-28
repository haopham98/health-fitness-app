from flask import Flask, request, jsonify, render_template, redirect, url_for
import bcrypt
import database
import mysql.connector

app = Flask(__name__)
app.secret_key = "super_secret_key"


@app.route('/')
def home():
    return 'Hello, from Flask!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form["username"]
            password = request.form["password"].encode("utf-8")
            email = request.form["email"]
            height = float(request.form["height"])
            weight = float(request.form["weight"])
            age = int(request.form["age"])
            gender = request.form["gender"]
            activity_level = request.form["activity_level"]

            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            conn = database.get_db_connection()
            if not conn:
                return jsonify({"error": "Không thể kết nối database"}), 500
            cursor = conn.cursor()
            try:
                cursor.execute(
                    (
                        "INSERT INTO Users (username, password, email, height, weight, age, gender, activity_level) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    ),
                    (
                        username,
                        hashed_password,
                        email,
                        height,
                        weight,
                        age,
                        gender,
                        activity_level,
                    ),
                )
                conn.commit()
                return jsonify({"message": "User registered successfully"}), 201
            except mysql.connector.Error as err:
                return jsonify({"error": str(err)}), 400
            finally:
                cursor.close()
                database.close_db_connection(conn)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)