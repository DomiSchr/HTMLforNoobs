import time
from PyDictionary import PyDictionary

dictionary=PyDictionary()

text = (dictionary.meaning("indentation"))
words = str(text).split(" ")

print(words[2])

startTime = time.time()
word = 2

wordsGotRight = 0

while True:
    print(words[word])
    inp = input("Type: ")
    if inp == str(words[word]):
        wordsGotRight += 1 

    word += 1
    timeNow = time.time()
    if timeNow - startTime >= 60:
        break

print("Finished: Your typing speed is: " + str(wordsGotRight))