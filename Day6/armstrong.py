def main():
    n=int(input("Enter a number"))
    temp=n
    sum=0
    dig=len(str(n))
    while temp>0:
        sum+=(temp%10)**dig
        temp//=10
    if sum==n:
        print("Armstrong number")
    else:
        print("Not an armstong number")
if __name__=="__main__":
    main()