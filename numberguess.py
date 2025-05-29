
import random


easy_level_turns=10
hard_level_turns=5


def check_ans(user_guess,computers,turns):
    if(computers==user_guess):
        print("you win",computers)
        
    elif(user_guess<computers):
        print(" too low")
        return turns - 1
    elif(user_guess>computers):
        print("too high")
        return turns - 1




def set_difficulty(): 
 print("select the level hard or easy")
 level=input("enter your choise")

 if(level=="hard"):
    return hard_level_turns
 else:
    return easy_level_turns
 
 


def game():
    print("Welcome to the number guess game")
    computer = random.randint(1,100)
    print(computer)

    turns=set_difficulty()

    user_guess=0
    while user_guess != computer:
      print(f"you have {turns} remaing")
      print("Guess the number")
      user_guess=int(input("enter your guess"))
      turns=check_ans(user_guess,computer,turns)
      if turns==0:
         print("you are out of game")
         return
      elif user_guess != computer:
         print("guess again")


game()





 