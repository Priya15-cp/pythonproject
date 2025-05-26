letters="abcdefghijklmnopqrstuvwxyz"
num_length= len(letters)
def encrypt(planetext , key):
   cailed = ''
   for letter in planetext:
        letter = letter.lower()
        if not letter == ' ':
               index= letters.find(letter)
               if index ==-1:
                    cailed += letter
               else:
                    new_index = index + key
                    if new_index>= num_length:
                          new_index -= num_length
                    cailed += letters[new_index]     

        return cailed                  
                      
def decrypt(cailed , key):
    planetext = ''
    for letter in cailed:
        letter = letter.lower()
        if not letter == ' ':
               index= letters.find(letter)
               if index==-1:
                      planetext += letter
               else:
                    new_index = index-key
                    if new_index <0:
                        new_index += num_length
                    planetext += letters[new_index]     

        return planetext                 
                      
print("what you want to do encrypt or decript")
userinput = input("enter e for encrypt and d for decrypt").lower()
if userinput == "e":
    key=int(input("enter the value of key"))
    text=input("enter a plane text")

    cailed = encrypt(text,key)
    print(f'the encrypted msg is {cailed}')


elif userinput == "d":
    key=int(input("enter the value of key"))
    text=input("enter a cailed text")
    
    planetext = decrypt(text,key)
    print(f"the encrypted msg is {planetext}")



