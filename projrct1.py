# city=input("enter your city name\n")
# pet=input("enter your pet name\n")
# band= city +  pet
# print("your band name is\n", band)

print("welcome to tip calculator")
bill=int(input("what is your total bill\n"))
tip=int(input("how much tip would you like yo give? 10,20,30\n"))
totalbill=bill+tip
int(totalbill)
people=int(input("how many people to split the bills\n"))
pay=totalbill/people
print("each person should pay :", pay)