import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO Users (name, email) VALUES (?, ?)",
               ("Alice", "alice@email.com"))
conn.commit()
print("Record Inserted!")
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()

print("\nUsers Table:")
for row in rows:
    print(row)
cursor.execute("UPDATE Users SET email = ? WHERE name = ?",
               ("alice_new@email.com", "Alice"))
conn.commit()
print("\nRecord Updated!")
cursor.execute("DELETE FROM Users WHERE name = ?",
               ("Alice",))
conn.commit()
print("Record Deleted!")

conn.close()