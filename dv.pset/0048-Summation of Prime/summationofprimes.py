#prime- number divisible by either one or itself only!
def primeNo(x):
    prime=0
    for i in range(2,x):
        if (x%i==0):
            prime=0
            break
        else:
            prime=1
    return prime

sum=0
for i in range (2,2000000):
    test=primeNo(i)
    if test==1:
        print (i)
        sum=sum+i
print ('Sum:',sum)
