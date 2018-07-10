a=int(input("enter binary num:"))
X=list(str(a))
L = list(map(int, X))
def convert(L):
#    pos*2+number
    sum=0
    for i in range (len(L)):
        sum=(i*2)+L[i]
    return sum
print(convert(L))
