print('Welcome to tresure island')
print("you miossion is to find tresure")
a=input("you are at cross road. where you want to go left or rignt")
if(a=="left"):

    print("you come to a lack.there is a island in the middleof the lack\n")
    b = input("type wait to wait for boat or type swim to swim across lack\n")
    if(b=="wait"):
     print("boat is not avalable,")
    
    elif(b=="swim"):
        print("you arrive to the islnd")
        c=input("there is a three door red yello blue which dore do you choose")
        if(c=="red"):
            print("its room full of fire, game over")
        
        elif(c=="blue"):
            print("congratulations you got tresure")
        else:
            print("no door")

    else:
       print("game over")
        
        
        


    
    

else:
    print("game over")
