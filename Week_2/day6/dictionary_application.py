# Simple Dictionary Application

dictionary = {
    "python": "A programming language",
    "computer": "An electronic device",
    "keyboard": "Input device"
}

def search_word():
    word = input("Enter word to search: ").lower()
    if word in dictionary:
        print("Meaning:", dictionary[word])
    else:
        print("Word not found.")

def add_word():
    word = input("Enter new word: ").lower()
    meaning = input("Enter meaning: ")
    dictionary[word] = meaning
    print("Word added successfully!")

while True:
    print("\n1. Search Word")
    print("2. Add Word")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        search_word()
    elif choice == '2':
        add_word()
    elif choice == '3':
            break
    else:
        print("Invalid choice!")