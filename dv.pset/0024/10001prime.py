print("pls wait for 2minutes, it takes time")
#for checking prime
def primeNo(x):
    flag=0
    for i in range (2,x):
        if x%i==0:
            flag=1
            break
#    if flag==0:
        #print ("Its prime")
#    else:
        #print ("no")
    return flag
primeNo()

#to check for the 10001st prime
def check():
    count=0
    i=2
    while count=<10001:
        if primeNo(i)==0:
            count=count+1
        i=i+1
    print (count)
    print (i-1)
check()
