def main():
    print("Functions for arithmetic Operations")
    def add():
        a=int(input("Enter number\n"))
        b=int(input("Enter sec number\n"))
        return a+b
    def sub():
        a=int(input("Enter number\n"))
        b=int(input("Enter sec number\n"))
        return a-b
    def mul():
        a=int(input("Enter number\n"))
        b=int(input("Enter sec number\n"))
        return a*b
    def div():
        a=int(input("Enter number\n"))
        b=int(input("Enter sec number\n"))
        return a/b
    
    print("sum=",add())
    print("sub=",sub())
    print("mul=",mul())
    print("div=",div())

if __name__=="__main__":
    main()

    
    