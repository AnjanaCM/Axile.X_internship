# File-Based Record System

def add_record():
    with open("records.txt", "a") as file:
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        file.write(name + "," + age + "\n")
    print("Record added successfully!\n")

def view_records():
    try:
        with open("records.txt", "r") as file:
            data = file.readlines()
            if not data:
                print("No records found.\n")
            else:
                for line in data:
                    name, age = line.strip().split(",")
                    print(f"Name: {name}, Age: {age}")
                print()
    except FileNotFoundError:
        print("No records file found.\n")

while True:
    print("1. Add Record")
    print("2. View Records")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_record()
    elif choice == '2':
        view_records()
    elif choice == '3':
        break
    else:
        print("Invalid choice!\n")