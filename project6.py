
import random

print("welcome to Pypassword Gemerator")
letters=['A',"B","C","D","E","F","G","H"]
symbols=["@","%",'^','*']
numbers=['1','2','3','4','5','6']


letter=int(input("how many letter would you like to enter\n"))
symbol=int(input("how many sybol you like to eenter\n"))
number=int(input("how many number you like to enter\n"))


password=[]
for letter in range(0,letter):
    password+=random.choice(letters)
for symbol in range(0,symbol):
    password+=random.choice(symbols)
for number in range(0,number):
    password+=random.choice(numbers)

print(password)

random.shuffle(password)
print(f'this is your password:{"".join(password)}')


