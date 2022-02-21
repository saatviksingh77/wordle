answer="BOOKS"
correct=False
i=1

print("You have 6 chances\n🟩 correct position\n🟨 wrong position\n⬛ not present\n")

while i<=6:
    guess=input(f"\n\nEnter guess {i}: \n").upper()
    if(len(guess)!=5):
        print("Enter 5 letter string")
    else:
        for j in range(0,5):
            if(guess==answer):
                print("Correct")
                correct=True
                break
            elif(guess[j]==answer[j]):
                print("🟩",end="")
            elif(guess[j] in answer):
                print("🟨",end="")
            else:
                print("⬛",end="")
        i=i+1
    if(correct):
        break
    if(i==7):
        print("\nAll chances over, try again")