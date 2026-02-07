def main():
    num=int(input("Enter a number"))
    i=1
    while i<=num:
        print(" "*(num-i)+"*"*(2*i-1))
        i+=1
if __name__=="__main__":
    main()