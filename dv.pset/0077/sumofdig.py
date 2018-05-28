p=int(input("Enter number : "))
#converting to list(string)
X=list(str(p))
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
