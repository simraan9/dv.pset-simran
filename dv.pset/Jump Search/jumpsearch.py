#A=[1,3,5,6,7,9,10,23,43,52,53,55,90]
#name_file=open('data.csv','r')
#items=name_file.read()
#l=items.split('\n')
#print (l)

import random
A=[]
for i in range (10000000):
    A.append(int(random.random()*100000000))

import time
t=0

def stepSize(x):
    m=int(x**0.5)
    return m
#print (stepSize(len(A)))

def jumpSearch(L,item,n):
    for i in range (0,len(L),n):
        if L[i-1]< item:
            pass
        elif L[i]==item:
            print ("Item is at L[",j,"] on the list")
            break
        if L[i-1]>item:
            for j in range(i-1-n,len(L),1):
                if L[j]==item:
                    print ("Item is at L[",j,"]on the list")
                    break
        else:
            print ("Invalid Item")

for i in range(10):
    start = time.perf_counter()
    A.sort()
    print(A)

    print (jumpSearch(A,210,stepSize(len(A))))
    #jumpSearch(l,778.5,stepSize(len(l)))
    end = time.perf_counter()
    t=t+(end - start)
    print(t)
print("total time",t)
