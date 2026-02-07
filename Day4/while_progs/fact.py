def main():
    print("-------factorial-------")
    num=int(input("Enter a number"))
    fact=1
    i=1
    while i<=num:
        fact=fact*i
        i+=1
    print(num,"!=",fact)
if __name__=="__main__":
    main()