# Import staff from tkinter library
from tkinter import Tk, Entry, Button, Label, END

# Import built-in math module in python
import math
import os
# Import module to open URLs in browser
import webbrowser

# Initialize window
root = Tk()
root.title('Expression Calculator')
root.resizable(False, False)  # To prevent user from resizing window

# Set window icon
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'calc.ico')
root.iconbitmap(path)

# Add entry field
e = Entry(root, fg='brown', borderwidth=5, width=80)
e.grid(row=0, column=0, columnspan=6, padx=10, pady=10)


# Used Functions
def add_character(c):
    e.insert(END, c)


def clear():
    e.delete(0, END)


# The following 3 functions implement Trignometric
# Functions taking angles of degree measures
def sin(angle):
    rad = math.radians(angle)
    return math.sin(rad)


def cos(angle):
    rad = math.radians(angle)
    return math.cos(rad)


def tan(angle):
    rad = math.radians(angle)
    return math.tan(rad)


def equal():
    exp = e.get()
    result = eval(exp)  # To convert string into a mathematical expression
    e.delete(0, END)
    e.insert(0, str(result))


def openLink(url):
    webbrowser.open_new(url)


# Adding buttons
button1 = Button(
    root, text='1', padx=40, pady=40, command=lambda: add_character('1'))
button2 = Button(
    root, text='2', padx=40, pady=40, command=lambda: add_character('2'))
button3 = Button(
    root, text='3', padx=40, pady=40, command=lambda: add_character('3'))
button4 = Button(
    root, text='4', padx=40, pady=40, command=lambda: add_character('4'))
button5 = Button(
    root, text='5', padx=40, pady=40, command=lambda: add_character('5'))
button6 = Button(
    root, text='6', padx=40, pady=40, command=lambda: add_character('6'))
button7 = Button(
    root, text='7', padx=40, pady=40, command=lambda: add_character('7'))
button8 = Button(
    root, text='8', padx=40, pady=40, command=lambda: add_character('8'))
button9 = Button(
    root, text='9', padx=40, pady=40, command=lambda: add_character('9'))
button0 = Button(
    root, text='0', padx=88, pady=40, command=lambda: add_character('0'))
buttonPlus = Button(
    root, text='+', padx=39, pady=40, command=lambda: add_character('+'))
buttonMinus = Button(
    root, text='-', padx=39, pady=40, command=lambda: add_character('-'))
buttonTimes = Button(
    root, text='×', padx=38, pady=40, command=lambda: add_character('*'))
buttonDevide = Button(
    root, text='÷', padx=39, pady=40, command=lambda: add_character('/'))
buttonLeftParenthese = Button(
    root, text='(', padx=40, pady=40, command=lambda: add_character('('))
buttonRightParenthese = Button(
    root, text=')', padx=40, pady=40, command=lambda: add_character(')'))
buttonPower = Button(
    root, text='xⁿ', padx=38, pady=40, command=lambda: add_character('**'))
buttonSine = Button(
    root, text='sin(', padx=33, pady=40, command=lambda: add_character('sin('))
buttonCosine = Button(
    root, text='cos(', padx=31, pady=40, command=lambda: add_character('cos('))
buttonTangent = Button(
    root, text='tan(', padx=32, pady=40, command=lambda: add_character('tan('))
buttonEqual = Button(
    root, text='=', padx=86, pady=40, command=equal)
buttonClear = Button(
    root, text='C', padx=39, pady=40, command=clear)
noteLabel = Label(
    root, text='You can use functions from "math" Python module')
linkLabel = Label(
    root, text='Learn more', fg='blue', cursor='hand2')
linkLabel.bind(
    "<Button-1>", lambda e: openLink(
        "https://docs.python.org/2/library/math.html"))


# Determine each button's place in the app grid
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
buttonClear.grid(row=4, column=0)
buttonPlus.grid(row=3, column=5)
buttonEqual.grid(row=4, column=4, columnspan=2)
button0.grid(row=4, column=1, columnspan=2)
buttonDevide.grid(row=4, column=3)
buttonMinus.grid(row=3, column=4)
buttonTimes.grid(row=3, column=3)
buttonLeftParenthese.grid(row=2, column=3)
buttonRightParenthese.grid(row=2, column=4)
buttonPower.grid(row=2, column=5)
buttonSine.grid(row=1, column=3)
buttonCosine.grid(row=1, column=4)
buttonTangent.grid(row=1, column=5)
noteLabel.grid(row=5, column=0, columnspan=3)
linkLabel.grid(row=5, column=3)

# Run app's main loop
root.mainloop()
