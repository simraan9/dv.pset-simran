x=(int(input("Enter first no: ")))
y=(int(input("Enter second no: ")))
A=[]
B=[]
D=[]
def numbers(x,y):
    i=1000
    while(i>1):
        A.append(x//i)
        x=x%i
        B.append(y//i)
        y=y%i
        i=i//10
    A.append(x)
    B.append(y)
    return A,B
numbers(x,y)

def reverse(L):
    M=[]
    for j in range(len(L)-1,-1,-1):
        M.append(L[j])
    return M

def multiplication(A,B):
    global D
    for i in range (3,-1,-1):
        C=[]
        carry=0
        for k in range(3,i,-1):
            C.append(0)
        for j in range (3,-1,-1):
            multiply1=(A[i]*B[j])+carry
            carry=multiply1//10
            rem=multiply1%10
            C.append(rem)
        if(carry>0):
            C.append(carry)
        for l in range(i,0,-1):
                C.append(0)
        D.append(reverse(C))
    return D
multiplication(A,B)

def add():
    F=[]
    carry=0
    global D
    for i in range(len(D[3])):
        sum=carry+D[0][len(D[0])-1-i]+D[1][len(D[1])-1-i]+D[2][len(D[2])-1-i]+D[3][len(D[3])-1-i]
        carry=sum//10
        rem=sum%10
        F.append(rem)
    if(carry>0):
        F.append(carry)
    return(reverse(F))
print(add())
