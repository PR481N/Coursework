

''' This is a program to find the next palindrome number after the number input in GUI.
This file contains:
Module imports
functions
if-else statements
loop
string slicing methods
Error handling
GUI
and more methods

Author : Prabin Subedi
Date : 2022/01/27'''

#IMPORTS
from tkinter import *
from tkinter import messagebox
# function that finds palindrome of num 
def process():
    Num='' 
    try:
        Num= int(entry.get())
        NumCopy = Num
    except Exception as e:
        messagebox.showerror("Error!", 'Only Enter Number greater than 0.')
        entry.delete(0, "end")

    if isinstance(Num, int):
        if Num > 0:
            while True:
                stra= str(Num)
                if stra[:]== stra[::-1]:
                    result.config(text = f"The next palindrome of {NumCopy} is {Num}.")
                    entry.delete(0, "end")
                    break
                else:
                    Num+=1
                    continue
        else:
            messagebox.showerror("Error!", 'Only Enter Number greater than 0.')
            entry.delete(0, "end")



# creating screen   
root = Tk()
root.geometry("600x400+500+200") # screen size
root.title("Next Palindrome Number Finder")
title = Label(root, text="Next Palindrome Number Finder", font=("Calibri",30), fg = "red")
title.pack()
# main frame
frame = Frame(root)
frame.pack(pady=20)
# number guessing Label
guessNum = Label(frame, text= "Enter the number you want to find the next palindrome of :",font=("Calibri", 15))
guessNum.pack()
# number entry
entry = Entry(frame, font= ("Calibri", 15))
entry.pack(pady = 10)
# find button
find= Button(frame, text= "Find", width= 15, font = 20, bg = "yellow", fg = "red" , command = process)
find.pack()
# result label
result = Label(frame, font=('Calibri', 15))
result.pack(pady=20)
# program exit 
Exit = Button(frame, text = "Exit", font= ('Calibri', 15), padx =40, bg = 'green', command = root.destroy)
Exit.pack()
root.mainloop() #holding screen
