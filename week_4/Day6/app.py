from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# -----------------------------
# DATABASE INIT
# -----------------------------
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

init_db()


# -----------------------------
# VIEW ALL RECORDS (READ)
# -----------------------------
@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()

    return render_template('index.html', students=students)


# -----------------------------
# ADD RECORD (CREATE)
# -----------------------------
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Students (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('add.html')


# -----------------------------
# EDIT RECORD (UPDATE)
# -----------------------------
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        cursor.execute("UPDATE Students SET name=?, email=? WHERE id=?", (name, email, id))
        conn.commit()
        conn.close()
        return redirect('/')

    cursor.execute("SELECT * FROM Students WHERE id=?", (id,))
    student = cursor.fetchone()
    conn.close()

    return render_template('edit.html', student=student)


# -----------------------------
# DELETE RECORD (DELETE)
# -----------------------------
@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect('/')


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)