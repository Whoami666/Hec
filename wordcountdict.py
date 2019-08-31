
wordl = input()
wordl = wordl.split()
wordcd = {}

for word in wordl:
    if (word in wordcd):
        wordcd[word] += 1
    else:
        wordcd[word] = 1
        
for word in wordcd:
    print(word, wordcd[word])
    

