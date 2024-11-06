import math
from tkinter import *

root = Tk()

inputEntry = Entry(root,  width=35, borderwidth=5)
inputEntry.grid(row=0, column=1, columnspan=3,padx=10, pady=10)

def btnclick(number):
    current = inputEntry.get()
    inputEntry.delete(0,END)
    inputEntry.insert(0,str(current) + str(number))

def add():
    num1 = inputEntry.get()
    global fnum
    global math
    math = "addition"
    fnum = int(num1)
    inputEntry.delete(0,END)


def subtract():
    num1 = inputEntry.get()
    global fnum
    global math
    math = "subtration"
    fnum = int(num1)
    inputEntry.delete(0,END)

def multiply():
    num1 = inputEntry.get()
    global fnum
    global math
    math = "multiply"
    fnum = int(num1)
    inputEntry.delete(0,END)

def divide():
    num1 = inputEntry.get()
    global fnum
    global math
    math = "divide"
    fnum = int(num1)
    inputEntry.delete(0,END)

def answer():
    num2 = inputEntry.get()
    inputEntry.delete(0,END)
    if math == "addition":
        inputEntry.insert(0, fnum + int(num2))
    if math == "subtration":
        inputEntry.insert(0, fnum - int(num2))
    if math == "multiply":
        inputEntry.insert(0, fnum * int(num2))
    if math == "divide":
        if num2 == 0:
            inputEntry.insert(0, "Error")
        else:
            inputEntry.insert(0, fnum / int(num2))


def btnclear():
    inputEntry.delete(0,END)


btn_1 = Button(root, text="1",padx=40, pady=20, command=lambda: btnclick(1))
btn_1.grid(row=3,column=1)
btn_2 = Button(root, text="2",padx=40, pady=20, command=lambda: btnclick(2))
btn_2.grid(row=3,column=2)
btn_3 = Button(root, text="3",padx=40, pady=20, command=lambda: btnclick(3))
btn_3.grid(row=3,column=3)

btn_4 = Button(root, text="4",padx=40, pady=20, command=lambda: btnclick(4))
btn_4.grid(row=2,column=1)
btn_5 = Button(root, text="5",padx=40, pady=20, command=lambda: btnclick(5))
btn_5.grid(row=2,column=2)
btn_6 = Button(root, text="6",padx=40, pady=20, command=lambda: btnclick(6))
btn_6.grid(row=2,column=3)

btn_7 = Button(root, text="7",padx=40, pady=20, command=lambda: btnclick(7))
btn_7.grid(row=1,column=1)
btn_8 = Button(root, text="8",padx=40, pady=20, command=lambda: btnclick(8))
btn_8.grid(row=1,column=2)
btn_9 = Button(root, text="9",padx=40, pady=20, command=lambda: btnclick(9))
btn_9.grid(row=1,column=3)

btn_0 = Button(root, text="0",padx=40, pady=20, command=lambda: btnclick(0))
btn_0.grid(row=4,column=1)
btn_0 = Button(root, text="=",padx=40, pady=20, command=answer)
btn_0.grid(row=4,column=3)
btn_9 = Button(root, text="clear",padx=28, pady=20, command=btnclear)
btn_9.grid(row=4,column=2)


btn_add = Button(root, text="+",padx=39, pady=20, command=add)
btn_add.grid(row=1,column=4)
btn_sub = Button(root, text="-",padx=42, pady=20, command=subtract)
btn_sub.grid(row=2,column=4)
btn_mult = Button(root, text="x",padx=39, pady=20, command=multiply)
btn_mult.grid(row=3,column=4)
btn_div = Button(root, text="/",padx=41, pady=20, command=divide)
btn_div.grid(row=4,column=4)

root.mainloop()
