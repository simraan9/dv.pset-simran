# to calculate sum of squares
def sqSum():
    i=1
    a=0
    while i<=100:
        x=i**2
        a=a+x
        i=i+1
    return (a)
sqSum()
#To calculate square of sums
def sumSq():
    i=1
    b=0
    while i<=100:
        x=i
        b=b+x
        #i=b**2
        z=b**2
        i=i+1
    return (z)
sumSq()
print (sumSq()-sqSum())
