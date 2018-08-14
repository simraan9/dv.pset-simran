A=[0,1,2,3,4,5,6,7,8,9]
def combinations(L):
    x=0
    for i in range (0,9):
        x=(10**9)*i+(10**8)+j

def factorial(num):
    fact=1
    for i in range(num,0,-1):
        fact=fact*i
    return fact

def combination(n, r):
    return int( factorial(n) / (factorial(r) * factorial(n - r)))
