def main():
    text="Python is very easy and Python is powerful"
    words=text.split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    print("\n word frequency:")
    print(word_count)
if __name__=="__main__":
    main()