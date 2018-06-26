print ("Enter 5 numbers with a space")
inputlist = input().split(' ')
L = list(map(int, inputlist))

def ascending(L):
    sum=0
    for i in range(0,5):
        if L[i-1]<=L[i]:
            sum=sum+1
    if sum==4:
        print ("Ascending")
    else:
        print ("None")
ascending(L)

def descending(L):
    sum=0
    for i in range(0,5):
        if L[i-1]>=L[i]:
            sum=sum+1
    if sum==4:
        print ("Descending")
descending(L)
