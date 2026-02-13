def add_student():
    roll=input("Enter roll number:\n")
    name=input("Enter Name:")
    marks=input("Enter marks:")
    with open("stud.txt","a")as file:
        file.write(f"{roll},{name},{marks}\n")
    print("Student record saved successfully.\n")
def view_stud():
    try:
        with open("stud.txt","r") as file:
            print("\n--------Student Records------")
            print(file.read())
    except FileNotFoundError:
        print("No records found.")
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice=input("Enter choice:")
    if choice == "1":
        add_student()
    elif choice=="2":
        view_stud()
    elif choice=="3":
        break
    else:
        print("Invalid choice")
        