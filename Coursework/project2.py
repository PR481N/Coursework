

''' This is a number guessing game program between two players in GUI. 
This program allows two different players to play game and store the game history in file.
This file contains:
Module imports
GUI
functions
if-elif-else statements
loop
string slicing
file handling
Exception handling

Author : Prabin Subedi
Date : 2022/01/27'''

# import module
from tkinter import *  #helps to create Gui in the program.
from tkinter import messagebox
import random  # helps to generate random number between given two numbers
import datetime #helps to provide the actual time and date

# global a for next turn
a = 0  

# guess number function
def guessNumFunc():
    global answer, result, totalGuesses, i, guess, exitButton, root, ranNum

    userAns = ''
    # get value from answer box
    try:
        userAns = int(answer.get())
    except Exception as e:
        messagebox.showerror("Error!", 'Only Enter Number')
        answer.delete(0, "end")
    # checking if random number is equal to useranswer
    if isinstance(userAns, int):
        if userAns > ranNum:
            result.config(text="Wrong Guess! Guess a lower number.", fg ='red')
            answer.delete(0, "end")
            i+=1
            totalGuesses.config(text = f"Total Guesses = {i}")
        elif userAns < ranNum:
            result.config(text="Wrong Guess! Guess a higher number.", fg = 'red')
            answer.delete(0, "end")
            i+=1
            totalGuesses.config(text = f"Total Guesses = {i}")

        else:
            result.config(text = f"Correct Guess. You guessed correct in {i+1} guesses. The number is {ranNum}", fg = 'green')
            answer.delete(0, "end")
            totalGuesses.config(text = f"Total Guesses = {i+1}")
            NextTurn()
            guess.destroy()

        

# Next button
def NextTurn():
    global a
    a+=1
    global exitButton
    exitButton = Button(root,width= 25, font = 20, bg = "grey", fg = "red",command= root.destroy)
    
    if a ==1:
        exitButton.config(text = "Click For Player 2 turn")
        exitButton.pack()
    else:
        exitButton.config(text ="Exit")
        exitButton.pack()

# defining function for screen
def gameScreen(player):
    
    global ranNum, answer, guess, result, totalGuesses, i,root
    ranNum = random.randint(1, 9)
    print(ranNum)

    root = Tk()
    root.geometry("900x400+500+150")
    root.title("Multiplayer Number Guessing Game")
    title = Label(root, text="Multiplayer Number Guessing Game", font=("Calibri",40))
    title.pack()
    
    # main frame
    mainFrame = Frame(root)
    mainFrame.pack(pady=30)
    
    # turn
    playerTurn = Label(mainFrame, text= f"{player} Turn:",font=("Calibri", 20), fg= 'blue')
    playerTurn.pack()

    # number guessing Label
    guessNum = Label(mainFrame, text= "Guess a Number betweeen 1 and 10:",font=("Calibri", 30))
    guessNum.pack()

    # answer entry
    answer = Entry(mainFrame, font= ("Calibry", 15))
    answer.pack(pady = 10)

    # guess button
    guess = Button(mainFrame, text= "Guess", width= 15, font = 20, bg = "yellow", fg = "red", command = guessNumFunc)
    guess.pack()

    # result label
    result = Label(mainFrame, font=('Calibri', 15))
    result.pack()

    # total guesses
    i= 0
    totalGuesses = Label(mainFrame, text = "Total Guesses = 0",font=("Calibri", 15), fg ='purple')
    totalGuesses.pack()

    # history
    History = Button(root, text= "History",font=("Calibri", 15), bg = 'pink',command= file)
    History.place(y=350, x = 20)
    
    root.mainloop()
    return i
    
# file reading
def file():
    global lines
    # creating the empty file if there is no such file before to avoid error.
    with open("gamedata.txt",'a') as f:
        f.write('')

    with open('gamedata.txt', 'r') as f:
        lines = '' 
        for line in (f.readlines()[-10:]):
            lines +=line
    history = Tk()
    history.title("History")
    history.geometry("900x400+500+150")
    content =Label(history, text=lines, font=("Calibri",17), )
    content.pack(pady = 30)
    
if __name__ == "__main__":
   
    guess1 = gameScreen("Player 1")
    guess2 = gameScreen("Player 2")
    
     #checking who guessed correct in less attempt
    if guess1 != 0 and guess2 !=0:
        if guess1> guess2:
            messagebox.showinfo("Winner","Player 2 won." )
        elif guess1< guess2:
            messagebox.showinfo("Winner!","Player 1 won.")
        else:
            messagebox.showinfo("Winner","Tie game.")

    
    if guess2 != 0 and guess1 !=0:
        # saving in file 
        with open("gamedata.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} Player 1 guessed in {guess1+1} guesses and player 2 guessed in {guess2+1} guesses.\n")
    
   

