a=int(input("Enter no. for binomial expansion: "))

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

def binomialExpansion(X):
    for i in range(X+1):
        print(factorial(X)/(factorial(X-i)*factorial(i)),"x^",X-i,"y^",i," +",end='')

binomialExpansion(a)
