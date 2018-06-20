#To find triangular no.
def triangleNo(x):
    j=0
    for i in range (0,x+1):
        j=j+i
    return (j)

#To find no. of divisors
def noOfDivisors(a):
    n=0
    for i in range (1,a+1):
        if a%i==0:
            n=n+1
    return n

#To find the value of the first triangle number with 500 divisors
def checkFiveHundred():
    a=1
    while noOfDivisors(a)<=500:
        b=triangleNo(a)
        if noOfDivisors(b)>=500:
            print (a,'th tri no. which is ',triangleNo(a))
            break
        else:
            a=a+1
print(checkFiveHundred())
