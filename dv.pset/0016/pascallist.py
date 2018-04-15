r=int(input("Enter no. for Pascal's Triangle: "))
def pascalsTriangle(x):
    a=[]
    for i in range(x):
        b=[]
        for j in range (i+1):
            if (j==0 or i==j):
                b.append(1)
            else:
                value=((a[i-1][j-1])+(a[i-1][j]))
                b.append(value)
        a.append(b)
        print("\n")
        print(a)
pascalsTriangle(r)
