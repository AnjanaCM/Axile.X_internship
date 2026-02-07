def main():
    print("----Using while loop")
    num=int(input("Enter a number"))
    i=1
    while(i<=num):
        if(i % 2==0):
            print(i)
        i+=1
if __name__=="__main__":
    main()
