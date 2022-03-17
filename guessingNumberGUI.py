from cgitb import enable
from tkinter import *
import random

root = Tk()
root.geometry("600x600")
root.title("Number Guessing Game")

l = Label(text = "Guess a number from 1 - 100")

inputTxt = Text(root, height = 10, width = 50, bg = "orange")

outputTxt = Text(root, height = 5, width = 50, bg = "white")

check = Button(root, height = 2, width = 20, text = "check", command = lambda:isCorrect())

rand = random.randint(1,100)

newGame = Button(root, height = 2, width = 20, text = "newGame", command = lambda:reset())

numsL = Label(text = "These are numbers you've already guessed")
triedNumsTXT = Text(root, height = 10, width = 50, bg = "pink")

def isCorrect():
    global rand
    input = inputTxt.get("1.0", "end-1c")
    input = int(input)
    if input != rand and input>rand:
        inputTxt.delete('1.0',END)
        outputTxt.delete('1.0',END)
        outputTxt.insert(END, "Too high, Try again")
        input = str(input)
        triedNumsTXT.insert(END, input+" ")
    elif input != rand and input<rand:
        inputTxt.delete('1.0',END)
        outputTxt.delete('1.0',END)
        outputTxt.insert(END, "Too low, Try again")
        input = str(input)
        triedNumsTXT.insert(END, input+" ")
    else:
        inputTxt.delete('1.0',END)
        outputTxt.delete('1.0',END)
        outputTxt.insert(END, "Correct!")
        check["state"] = DISABLED

def reset():
    check["state"] = NORMAL
    inputTxt.delete('1.0',END)
    outputTxt.delete('1.0',END)
    triedNumsTXT.delete('1.0',END)
    global rand
    input = inputTxt.get("1.0", "end-1c")
    input = int(input)
    if input != rand and input>rand:
        inputTxt.delete('1.0',END)
        outputTxt.delete('1.0',END)
        outputTxt.insert(END, "Too high, Try again")
        input = str(input)
        triedNumsTXT.insert(END, input+" ")
    elif input != rand and input<rand:
        inputTxt.delete('1.0',END)
        outputTxt.delete('1.0',END)
        outputTxt.insert(END, "Too low, Try again")
        input = str(input)
        triedNumsTXT.insert(END, input+" ")
    else:
        inputTxt.delete('1.0',END)
        outputTxt.delete('1.0',END)
        outputTxt.insert(END, "Correct!")
        check["state"] = DISABLED



l.pack()
inputTxt.pack()
check.pack()
outputTxt.pack()
numsL.pack()
triedNumsTXT.pack()
newGame.pack()

mainloop()