import sqlite3

# Connect to database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

print("Database Connected Successfully!")
cursor.execute("INSERT INTO Users (name, email) VALUES (?, ?)",
               ("Rahul", "rahul@email.com"))
conn.commit()
print("Record Inserted!")
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()

print("\nUsers Table:")
for row in rows:
    print(row)
cursor.execute("UPDATE Users SET email = ? WHERE name = ?",
               ("rahul_new@email.com", "Rahul"))
conn.commit()
print("\nRecord Updated!")

cursor.execute("DELETE FROM Users WHERE name = ?",
               ("Rahul",))
conn.commit()
print("Record Deleted!")

conn.close()
print("\nDatabase Connection Closed!")