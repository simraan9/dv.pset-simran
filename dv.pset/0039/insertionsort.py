M=[6,4,2,9,5]
def insertionSort():
    for i in range (1,5,1):
        for j in range (0,i,1):
            if (M[j]>M[i]):
                pos=j
                take=M[i]
                for k in range(i,pos,-1):
                    M[k]=M[k-1]
            M[pos]=take
        print (M)
insertionSort()
