x=input("Enter text to encrypt: ")
key=int(input("Enter Caesar's key (0-25): "))

'''to convert input word to list
l=[]
for i in range (len(x)):
    l.append(x[i])
#print (l)
'''
def rotate(inputlist,k):
    M=[]
    A="abcdefghijklmnopqrstuvwxyz"
    for i in range (len(A)): #cipher solution
        M.append(A[(i+k)%26])
    #print (M)

    N=""
    for g in range (len(inputlist)):
        if inputlist[g]==A[g]:
            N+=M[g]
    return (N)
print(rotate(x,key))
