def fibonacci():
    L=[1,1]
    l=0
    i=2
    while (l<10**999):
        l=L[i-1]+L[i-2]
        L.append(l)
        i=i+1
    print ('First 1000 digit no is: ',L[-1])
    print ('Index of the first 1000 digit no:',str(len((L))-1))
fibonacci()
