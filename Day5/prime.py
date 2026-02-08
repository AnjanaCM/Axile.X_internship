def main():
    print("Prime numbers")
    def isprime():
        n = int(input("Enter a number: "))
        if n <= 1:
            print(n, "is not a prime number")
            return
        for i in range(2, n):
            if n % i == 0:
                print(n, "is not a prime number")
                break
        else:
            print(n, "is a prime number")
    isprime()
if __name__ == "__main__":
    main()
