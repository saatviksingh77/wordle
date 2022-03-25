import turtle
import sys
import random
import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from collections import Counter

f=open("Wordle\WordLists\wordleWordList.json")
f2=open("Wordle\WordLists\wordleAnswerList.json")
wordList=json.load(f)
ansList=json.load(f2)

sc=turtle.Screen()
t=turtle.Turtle()
txtTurtle=turtle.Turtle()
txtTurtle.color("white")
root = Tk()

t.hideturtle()
t.width(2)
t.pu()
txtTurtle.hideturtle()
txtTurtle.pu()
sc.setup(500,600)
sc.bgcolor("#121213")
sc.title("Wordle in Python")

grn="#538d4e"
ylw="#b59f3b"
gry="#3a3a3c"


##### function definitions START #####

def square(col):
    t.begin_fill()
    for i in range(4):
        t.pd()
        t.color(col)
        t.forward(35)
        t.circle(5,90)
    t.end_fill()
    t.pu()
    t.forward(50)

def outline():
    for i in range(4):
        t.pd()
        t.color("#656566")
        t.forward(35)
        t.circle(5,90)
    t.pu()
    t.forward(50)

def writeLetter():
    txtTurtle.write(guess[k].upper(),font=("Helvetica",20,"bold"))
    txtTurtle.forward(50)

def initializeGame():
    global i,answer,validGuess
    i=1
    validGuess=True
    answer=random.choice(ansList)
    t.clear()
    txtTurtle.clear()
    t.speed(0)
    for x in range(1,7):
        t.goto(-110,200-(50*x))
        for y in range(5): outline()
    t.speed(10)

def simulate_guess(guess: str, answer: str):
    result = [0,0,0,0,0]
    a_count = Counter(answer)
    left_to_check = []
    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = 2
            a_count[guess[i]] -= 1
        else :
            left_to_check.append(i)
    for i in left_to_check:
        if a_count[guess[i]]!= 0:
            result[i] = 1
            a_count[guess[i]]-=1
        else:
            result[i] = 0
    return result

##### function definitions END #####

initializeGame()

while i<=6:
    guess=turtle.textinput("Guess",f"Enter guess {i}").lower()
    g_count = Counter(guess)
    a_count = Counter(answer)
    print(guess)
    validGuess=True
    if(len(guess)!=5):
        messagebox.showinfo("Try again", "You must enter a 5 letter word")
        validGuess=False
    elif(guess not in wordList):
        messagebox.showinfo("Try again", "Word not recognized")
        validGuess=False
    t.goto(-110,200-(50*i))
    txtTurtle.goto(-100,205-(50*i))
    if(validGuess):
        res = simulate_guess(guess,answer)
        for j,k in zip(res,range(5)):
            if(j==2):
                square(grn)
                writeLetter()
            elif(j==1):
                square(ylw)
                writeLetter()
            else:
                square(gry)
                writeLetter()
        i=i+1
    if(guess==answer):
        playAgain=messagebox.askyesno("Congratulations","Yay, you have guessed the word!\nPlay again?")
        if(playAgain): initializeGame()
        else: sys.exit()
    if(i==7):
        playAgain=messagebox.askyesno("Uh oh",f"You have used all your tries!\nPlay again?\n\nThe word was: {answer.upper()}")
        if(playAgain): initializeGame()
        else: sys.exit()

root.mainloop()