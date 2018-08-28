x=input("Enter text to encrypt: ")
key=int(input("Enter Caesar's key (0-25): "))

def rotate(string1,k):
    M=[]
    A="abcdefghijklmnopqrstuvwxyz"
    for i in range (len(A)): #cipher solution
        M.append(A[(i+k)%26])
    #print (M)

    N=""
    for g in range (len(string1)):
        for j in range (len(A)):
            if string1[g]==A[j]:
                N+=M[j]
    return (N)

def unrotate(string1,k):
    return (rotate(string1,(-1)*k))
    
print (rotate(x,key))
print (unrotate(x,key))
