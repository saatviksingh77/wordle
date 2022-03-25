from collections import Counter
import json, random

f=open("Wordle\WordLists\wordleWordList.json")
f2=open("Wordle\WordLists\wordleAnswerList.json")
wordList=json.load(f)
ansList=json.load(f2)
answer=random.choice(ansList)

correct=False
i=1

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

print("You have 6 chances\n🟩 correct position\n🟨 wrong position\n⬛ not present\n")

while i<=6:
    guess=input(f"\n\nEnter guess {i}: \n").lower()
    if(len(guess)!=5):
        print("Enter 5 letter string")
    elif(guess not in wordList):
        print("Not a valid word")
    else:
        res = simulate_guess(guess,answer)
        for j in res:
            if j == 2:
                print('🟩',end="")
            elif j == 1:
                print('🟨',end="")
            else:
                print('⬛',end="")
        correct = all(x==2 for x in res)
        i=i+1
    if(correct):
        break
    if(i==7):
        print("\nAll chances over, try again")
        print(f"Answer = {answer}")