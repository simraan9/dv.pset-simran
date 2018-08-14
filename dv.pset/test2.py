x=input("Enter text to encrypt: ")
key=int(input("Enter Caesar's key (0-25): "))

A="abcdefghijklmnopqrstuvwxyz"
def rotate(k,A):
    M=[]
    for i in range (len(A)): #cipher solution
        M.append(A[(i+k)%26])
    return (M)

def cipher(inputlist,M,A):
    N=""
    for g in range (len(inputlist)):
        if inputlist[g]==A[g]:
            N+=M[g]
    return (N)
print(cipher(x,rotate(k,A),A))
