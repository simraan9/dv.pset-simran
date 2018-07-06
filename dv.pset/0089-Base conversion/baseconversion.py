a=int(input("Enter number to convert to binary:"))
def convert(x):
    A=[]
    B=[]
    while x>0:
        if x%2==0:
            A.append(0)
        else:
            A.append(1)
        x=x//2
    #print (A)
    for i in range (len(A)-1,-1,-1):
        B.append(A[i])
    print (B)
convert(a)
