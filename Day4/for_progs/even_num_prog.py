def main():
    print("printing only even numbers")
    num=int(input("Enter how many numbers to "
    "print even numbers"))
    i=2
    for i in range(num):
            if i % 2 == 0:
                print(i)
if __name__ == "__main__":
     main()