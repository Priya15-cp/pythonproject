print("Welcome to the secret auction!!!!")

      

   
def greater_bit(dictonary_bid):
   winner=""
   higher_bit=0

   max (bids)
   for bit in bids:
      bid_amount= bids[bit]
      if bid_amount > higher_bit:
         higher_bit=bid_amount
         winner=bit

   print(f"you win {winner} the amount is {higher_bit}")
      
bids= {}
again_biding=True
while again_biding:
   name=input("enter the name of person\n")
   amount=int(input("your bid"))
   bids[name]=amount
   continou=input("are there is other bidder")

   if continou=="no":
        again_biding= False
        greater_bit(bids)

   elif continou== "yes":
      
       print("\n"*20)  
       