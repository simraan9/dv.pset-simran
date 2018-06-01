'''
Write following sigma functions where n is input argument in each case.

(a) S1: 1,2,3,…
(b) S2: 3,5,7,..
(c) S3: 2,3,5,6,7,8,10,11,12,13,… (ie. Number that are not squares)

In each of the following, calculate sum till n terms.
'''
A=[]
B=[]
C=[]
n=int(input("Enter no: "))
def S1():
    global A
    for i in range (1,n+1,1):
        A.append(i)
    return (A)
print ('S1: ',S1())

def S2():
    global B
    for i in range (3,n+1,2):
        B.append(i)
    return (B)
print ('S2: ',S2())

def S3():
    global C
    o=0
    D=[]
    for i in range (2,n+1):
        C.append(i)
    while o<len(C):
        for j in C:
            if C[o]==(j**2):
                C.pop(o)
        o=o+1
    return (C)
print ('S3: ',S3())

def addingLists(A):
    s=0
    for j in range (len(A)):
        s=s+A[j]
    print ('sum=', s)
addingLists(A)
addingLists(B)
addingLists(C)
