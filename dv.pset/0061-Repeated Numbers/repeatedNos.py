print ('Enter 10 numbers with a space:')
numbers = input().split(' ')
L = list(map(int, numbers))

def sortList(x):
    for i in range(0,10,1):
        for j in range(i+1,10,1):
                if x[i]>x[j]:
                    z=x[i]
                    x[i]=x[j]
                    x[j]=z
                #print(x)
    return(x)
sortList(L)
print ("Repeated nos:")
def repeatNo(X):
    for i in range (0,len(X)):
        if X[i-1]==X[i]:
            print (X[i])
repeatNo(L)
