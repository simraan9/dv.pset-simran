def multiples():
    A=[]
    x=0
    for i in range (0,1000):
        if (i%3==0) or (i%5==0):
            A.append(i)
    print(A)
    for j in range (len(A)):
        x=x+A[j]
    print ('sum=', x)
print (multiples())
