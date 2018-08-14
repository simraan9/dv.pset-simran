L=['A','B','C','D']

def rotate(M):
    last=len(M)-1
    temp=M[last]
    for i in range(last,0,-1):
        M[i]=M[i-1]
    M[0]=temp

def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*n
    return fact

def hameltonion_circuit(M):
    G=[]
    i=1
    B=[]
    B.append(M[i-1])
    while(i<len(M)):
        for j in range(len(B)):
            B[j].append(M[i-1])
        for k in range(factorial(i-1)):
            G=B[k]
            for l in range(i):
                H.append(G)
                rotate(H)
                B.append(H)
        i=i+1
    return B

print(hameltonion_circuit(L))



















'''G.append(M)
    A=2
    B=factorial(A)*-1
    for i in range(23):
        while(A<len(M)+1):
            take=M[B]
            for i in range(B,len(M)-1,1):
                M[i]=M[i+1]
            M[-1]=take
            A=A+1
        G.append(M)
    return G

print(hemeltonion_circuit(L))'''
