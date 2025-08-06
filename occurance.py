w=input("type a sentence:")
w=w.lower()
words=w.split()
words_count={}
for i in words:
    if i in word_count:   
        word_count[i]+=1
    else:
        word_cont[i]=1
print(word_count)
