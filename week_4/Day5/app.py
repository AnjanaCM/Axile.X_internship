from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

init_db()
@app.route('/')
def register_page():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO Users (name, email, password) VALUES (?, ?, ?)",
            (name, email, password)
        )
        conn.commit()
        conn.close()
        return redirect('/login')

    except sqlite3.IntegrityError:
        conn.close()
        return render_template('register.html', error="Email already exists!")
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM Users WHERE email=? AND password=?",
            (email, password)
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"""
            <h1>Welcome {user[1]} </h1>
            <a href='/login'>Logout</a>
            """
        else:
            return render_template('login.html', error="Invalid Email or Password")

    return render_template('login.html', error="")
if __name__ == '__main__':
    app.run(debug=True)