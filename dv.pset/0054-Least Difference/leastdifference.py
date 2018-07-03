print ('Enter 10 numbers with a space:')
numbers = input().split(' ')
L = list(map(int, numbers))

def leastDiff(L):
    diff=1000000000000000000000
    for i in range (0,10):
        x=L[i-1]-L[i]
        if x<diff:
            diff=x
            print (L[i-1],L[i],diff)

leastDiff(L)
