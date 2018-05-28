a=1
A=[]
#to calculate factorial
def fact(x):
    global a
    global A
    for i in range (x,1,-1):
        a=a*i
    #a=str(a)
    #print (a)
    A.append(a)
    print ('100! = ', a)
    return (A)
fact(100)

#converting to list(string)
X=list(str(a))
#print ('X=',X)

#converting to int list
L = list(map(int, X))
print (L)

#adding the digits
def addDig():
    s=0
    for j in range (len(L)):
        s=s+L[j]
    print ('sum=', s)
addDig()
