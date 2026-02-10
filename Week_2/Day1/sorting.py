def main():
    num=[4,7,1,9,3]
    ascend=sorted(num)
    descend=sorted(num, reverse=True)
    print("Ascending", ascend)
    print("Descending",descend)
if __name__=="__main__":
    main()