n=int(input("Enter no to count divisibility by 7:"))
def isDivisible(n):
    count=0
    for i in range (1,n+1,1):
        if i%7==0:
            count=count+1
    return count
print ('Count:',isDivisible(n))
