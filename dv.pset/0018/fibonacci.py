L=[1,1]
#n=int(input("Enter n for your fibonacci series: "))
#Fibonacci list
def createList():
    l=0
    add=0
    i=2
    while (l<40000000):
        l=L[i-1]+L[i-2]
        L.append(l)
        i=i+1

        if (l%2==0):
            add=add+l
    L.pop()
    print (L)
    print (add)
createList()

'''Adding even valued numbers
def evenAdd():
    add=0
    for i in range (2,n,3):
        add=add+L[i]
    print (add)
evenAdd() '''
