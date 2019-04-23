import os

"""
    script is reading from given file name and count appearances of each word
"""

file_path="C:/TEST/1.txt"

file=open(file_path,"r+")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

#Sort the result by count of appearance
wordcount = dict(sorted(wordcount.items(), key=lambda x: x[1]))

for k,v in wordcount.items():
    print (k, v)
