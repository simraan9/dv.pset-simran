a=int(input("enter binary num:"))
X=list(str(a))
L = list(map(int, X))
print (L)

def convert(L):
#    pos*2+number
    sum=0
    val=0
    for i in range (len(L)):
        sum=(i*2)+L[i]
        val=sum
        while i<=(len(L)):
            sum1=(val*2)+L[i]
            print (sum1)
print(convert(L))
