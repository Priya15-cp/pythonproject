import random
print("welcome to Hangman")
print("you have to guess number ni 6 attemps")
ren=["happy",'sad','beauty','hello']
rnd=random.choice(ren)
print(rnd)
lives=6

display=[]*len(rnd)
for i in range(len(rnd)):
    display += '_'
print(display)
game_over = False
while not game_over:
   guessed_word=input("Guess the letter\n").lower()
   for position in range(len(rnd)):
      letter = rnd[position]
      if letter==guessed_word:
        display[position]==guessed_word
        print(display)

   if guessed_word  not in rnd:
      lives -= 1
      if lives==0:
        game_over = True
        print("you loose")
   if '_' not  in display:
      game_over=True
      print("you win")