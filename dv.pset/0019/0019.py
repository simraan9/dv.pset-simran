n=int(input("Enter first numerator: "))
d=int(input("Enter first denominator:"))
a=int(input("Enter second numerator: "))
b=int(input("Enter second denominator:"))

def fraction():
    '''j=n/d
    k=a/b'''
    x=((n*b)+(d*a))
    y=(d*b)
    print (x,"/",y)
fraction()

#def decToFract():
