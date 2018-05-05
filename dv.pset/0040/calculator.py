def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
c=input("What do you want to do today? (+,-,*,/)")
a=int(input("Enter A "))
b=int(input("Enter B "))
if c == "+":
    print (add(a,b))
if c == "-":
    print (sub(a,b))
if c == "*":
    print (mul(a,b))
if c == "/": 
    print (div(a,b))
