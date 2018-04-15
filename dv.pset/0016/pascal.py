def factorial(num):
    fact=1
    for i in range(num,0,-1):
        fact=fact*i
    return fact

def combination(n, r):
    return int( factorial(n) / (factorial(r) * factorial(n - r)))

def pascals_triangle1(x):
    for i in range(x):
        for k in range(x-1-i):
            print(" ",end="")
        for j in range(i+1):
            value=combination(i,j)
            print(str(value)+" ",end="")
        print("\n")

a=int(input("Enter no. for pascal's triangle"))
print (pascals_triangle1(a))
