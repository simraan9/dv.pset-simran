def collatz(i):
    count=1
    while i>1:
        if i%2==0:
            i=i//2
        else:
            i=(3*i)+1
        #print (i)
        count=count+1
    return count

def largestSeq():
    collatzCount=0
    maxVal=0
    for i in range (1000000,0,-1):
        collatzCount=collatz(i)
        if collatzCount>maxVal:
            maxVal=collatzCount
            r=i
    print ('Max collatz count for any number below 1M is', maxVal, 'and the number is:',r)
largestSeq()
