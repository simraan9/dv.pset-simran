print ('Enter 10 numbers with a space:')
numbers = input().split(' ')
L = list(map(float, numbers))

def avg(A):
    sum=0
    count=0
    for i in range (len(A)):
        sum=sum+A[i]
        count=count+1
    average=sum/count
    return average
print ('Average sum:',avg(L))
