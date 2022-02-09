from tkinter import *
import random

root = Tk()
root.geometry("600x600")
root.title("Number Guessing Game")

l = Label(text = "Guess a number from 1 - 100")

inputTxt = Text(root, height = 10, width = 50, bg = "yellow")

outputTxt = Text(root, height = 5, width = 50, bg = "blue")

check = Button(root, height = 2, width = 20, text = "check", command = lambda:isCorrect())

rand = random.randint(1,100)

def isCorrect():
    global rand
    input = inputTxt.get("1.0", "end-1c")
    input = int(input)
    if input != rand and input>rand:
        outputTxt.insert(END, "Too high, Try again")
    elif input != rand and input<rand:
        outputTxt.insert(END, "Too low, Try again")
    else:
        outputTxt.insert(END, "Correct!")
    

l.pack()
inputTxt.pack()
check.pack()
outputTxt.pack()

mainloop()