import random

opyion=["stone","paper","scissor"]
computer=random.choice(opyion)
print("lets play a game")
user=input("choose any one among three stone ,paper scissors\n")
print("computer:",computer)

if user==computer:
    print("nobody win its tie")
elif(user=="stone" and computer=="scissors") or (user=="paper" and computer=="stone")or(user=="scissors"and computer=="paper"):
    print("you win")
else:
    print("computer wins")