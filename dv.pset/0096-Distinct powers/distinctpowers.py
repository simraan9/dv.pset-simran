L=[]
for a in range (2,101): #defining a between 2-100
    for b in range(2,101): #defining b between 2-100
        L.append(a**b) #listing all relevant terms (a^2)
L.sort()

# to eliminate extra terms
M=[]
for i in range (len(L)):
    if L[i] not in M:
        M.append(L[i])
print ('Number of distinct terms: ',len(M))
