def main():
    n=int(input("Enter a number"))
    tot=0
    i=1
    while i<=n:
        tot+=i
        i+=1
    print("sum of",n,"=",tot)
if __name__=="__main__":
    main()
