def main():
    a=int(input("Enter 1st number\n"))
    b=int(input("Enter 2nd number\n"))
    c=int(input("Enter 3rd number\n"))
    if((a>b)&(a>c)):
        print(a,"is larger")
    elif((b>a)&(b>c)):
        print(b,"is largest")
    else:
        print(c,"is largest")
if __name__ == "__main__":
    main()    