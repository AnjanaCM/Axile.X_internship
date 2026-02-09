def main():
    n=int(input("Enter num of terms"))
    a,b=0,1
    for i in range(n):
        print(a,",",end="")
        a,b=b,a+b