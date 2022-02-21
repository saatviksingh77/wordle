from collections import Counter
import json, random

f=open("Wordle\WordLists\wordleWordList.json")
f2=open("Wordle\WordLists\wordleAnswerList.json")
wordList=json.load(f)
ansList=json.load(f2)
answer=random.choice(ansList)

correct=False
i=1

print("You have 6 chances\n🟩 correct position\n🟨 wrong position\n⬛ not present\n")

while i<=6:
    guess=input(f"\n\nEnter guess {i}: \n").lower()
    g_count = Counter(guess)
    a_count = Counter(answer)
    if(len(guess)!=5):
        print("Enter 5 letter string")
    elif(guess not in wordList):
        print("Not a valid word")
    else:
        for j in range(0,5):
            if(guess==answer):
                print("Correct")
                correct=True
                break
            elif(guess[j]==answer[j]):
                print("🟩",end="")
            elif(g_count[guess[j]] == a_count[guess[j]]):
                print("🟨",end="")
            else:
                print("⬛",end="")
        i=i+1
    if(correct):
        break
    if(i==7):
        print("\nAll chances over, try again")