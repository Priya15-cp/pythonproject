
def addtion(n1,n2):
    return n1+n2
 
def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operators= {
    "+" : addtion,
    "-"  : substract,
    "*"  : multiply,
    "/"  : divide
    }
should_accumulate = True
num1=int(input("enter the first number"))
while should_accumulate:
  for symbol in operators:
      print(symbol)
  operators_symbol=input("pick the symbol")
  num2=int(input("enter the second number"))
  answer=operators[operators_symbol](num1,num2)
  print(f"{num1}{operators_symbol}{num2}={answer}")
  choice=input("type y if you want to continou or type n if youy want is new calculator")
  if(choice=="y"):
    num1=answer
  else:
    should_accumulate=False
    print("\n"*10)