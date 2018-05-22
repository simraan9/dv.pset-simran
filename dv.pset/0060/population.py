m=1000000
def grow(x):
    x=x+((3/100)*x)
    return x
def growth(y):
    y=y+((2/100)*y)
    return y
def population(x,y):
    z=0
    while(x<y):
        x=grow(x)
        y=growth(y)
        #print(x,y)
        z=z+1
    print(str(z)+'years')
A=5*m
B=7*m
population(A,B)
