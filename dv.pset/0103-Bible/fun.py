import operator

name_file=open('bible.txt','r')
items=name_file.read()
avoid=[' ','.','?','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','|',"\n",';',':','<','>','/' ]
#print (items)

H=['and','and','and','to','sdjb','sdg','sdn','to','to','to','to','to','to','to','to','to','to']

def countList(K):
    K.sort()
    #print (K)
    A={}
    #B=[]
    i=0
    while(len(K)>0):
        count=1
        j=1
        while(j<len(K) and K[i]==K[j]):
            count=count+1
            K.pop(j)
            #print (A)
        A[K[i]]=count
        #A.append(count)
        #B.append(K[i])
        K.pop(i)
        #print(len(K))
        #print(K[i],K[j],count,limit)
        count=1
        print(A)
    A = sorted(A.items(), key=operator.itemgetter(1), reverse=True)
    return A


print (countList(H))
