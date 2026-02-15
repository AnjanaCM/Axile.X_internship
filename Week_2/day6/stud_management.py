# Student Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"Name": name, "Marks": marks}
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No records found.\n")
    else:
        for roll, data in students.items():
            print(f"Roll: {roll}, Name: {data['Name']}, Marks: {data['Marks']}")
        print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print(f"Name: {students[roll]['Name']}, Marks: {students[roll]['Marks']}\n")
    else:
        print("Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")