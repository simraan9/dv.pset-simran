A=[7,9,1,6,3]
def bubbleSort(x):
    for i in range(0,5,1):
        for j in range(i+1,5,1):
                if x[i]>x[j]:
                    z=x[i]
                    x[i]=x[j]
                    x[j]=z
                print(x)
    return(x)
print (bubbleSort(A))
