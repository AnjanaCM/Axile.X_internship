text="hello"
freq={}
for char in text:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print("text")
print(freq)
