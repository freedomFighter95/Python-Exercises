# print the word that start with "s" in string using split method
sentence = "print only the words start with s in this sentence"
for i in sentence.split(" "):
    if i[0] == "s":
        print(i)