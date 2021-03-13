import time
from PyDictionary import PyDictionary
from tkinter import *

dictionary=PyDictionary()

text = (dictionary.meaning("indentation"))
words = str(text).split(" ")

root = Tk()
topframe = Frame(root)
bottomframe = Frame(root, bg = "black")

topframe.pack()
bottomframe.pack(side = BOTTOM)

button1 = Button(bottomframe, text = "Submit", fg = "black")
label1 = Label(topframe, text = "Text")

button1.pack()
label1.pack()

root.mainloop() 


# startTime = time.time()
# word = 2

# wordsGotRight = 0

# while True:
#     print(words[word])
#     inp = input("Type: ")
#     if inp == str(words[word]):
#         wordsGotRight += 1 

#     word += 1
#     timeNow = time.time()
#     if timeNow - startTime >= 60:
#         break

# print("Finished: Your typing speed is: " + str(wordsGotRight))