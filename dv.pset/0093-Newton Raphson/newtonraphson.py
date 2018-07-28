import random

#To read a number
A=int(input("Enter N to find square root: "))

def f(x,N):
    return (x*x - N)
def ff(x):
    return 2*x
def newton(x, N):
    return x - f(x,N)/ff(x)

#Initial guess
x = random.uniform(0,A)

for i in range(6):
    #New guess
    x = newton(x, A)
    print((i,x))
