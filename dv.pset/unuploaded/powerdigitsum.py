'''
2^15=32768 and the sum of its digits is 3+2+7+6+8=26.
What is the sum of the digits of the number 2^1000?
'''
a=2**1000
X=list(str(a))
#converting to int list
L = list(map(int, X))

#adding the digits
def addDig():
    s=0
    for i in range (len(L)):
        s=s+L[i]
    print ('sum=', s)
addDig()
