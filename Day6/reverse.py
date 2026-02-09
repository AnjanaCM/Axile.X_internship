def main():
    text=input("Enter a string:")
    rev=""
    for ch in text:
        rev=ch+rev
    print("Reversed string:",rev)
if __name__=="__main__":
    main()