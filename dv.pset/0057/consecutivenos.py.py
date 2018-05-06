x = int(input("enter no: "))
n=1
for i in range(0,x,1):
    for j in range(0,i+1,1):
        print(n, end=" ")
        n = n + 1
    print()
