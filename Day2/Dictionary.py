def main():
    studs={
        101: {"name":"Anju", "age":22,"grade":"A"},
        102:{"name":"Swag", "age":22,"grade":"A"},
        103:{"name":"xyz", "age":23,"grade":"B"}
    }
    print("Student Dictionary")
    print(studs)
    studs[104]={"name":"abc","age":25,"grade":"C"}
    print("\n After adding")
    print(studs)
    studs[102]["grade"]="A+"
    print("\n After Updating Grade")
    print(studs)
    del studs[103]
    print("\n After deleting")
    print(studs)
if __name__=="__main__":
    main()