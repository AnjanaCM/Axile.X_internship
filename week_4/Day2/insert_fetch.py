import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Insert into Users
cursor.execute("INSERT INTO Users (name, email) VALUES (?, ?)", 
               ("John", "john@email.com"))

# Insert into Students
cursor.execute("INSERT INTO Students (name, course) VALUES (?, ?)", 
               ("Alice", "Python"))

# Insert into Tasks
cursor.execute("INSERT INTO Tasks (title, status) VALUES (?, ?)", 
               ("Complete Internship Task", "Pending"))

conn.commit()

# Fetch Users
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()

print("Users:")
for user in users:
    print(user)

conn.close()