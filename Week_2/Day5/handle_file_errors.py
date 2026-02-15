try:
    filename = input("Enter filename: ")
    file = open(filename, "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected error:", e)