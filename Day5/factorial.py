def main():
    print("Factorial")
    n=int(input("Enter a number"))
    def facto(n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact
    print("factorial of",n,"is",facto(n))
if __name__=="__main__":
    main()