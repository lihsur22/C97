intro=input("Give Intoduction Here : ")
print(intro)

wordCount = 1
chrCount = 0

for i in intro:
    chrCount = chrCount + 1
    if(i==" ") :
        wordCount = wordCount + 1
    print("Character Count : ")
    print(chrCount)
    print("Word Count : ")
    print(wordCount)