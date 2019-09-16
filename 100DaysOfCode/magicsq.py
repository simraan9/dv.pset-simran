import random
n = int(input("enter n (side): "))
maxRepeat = n
maxSum = int(input("enter maximum sum: "))

def magicSquare():
    M= []
    k=[0,0,0]
#    print (L)
    for i in range (0,n):
        sum=0
        L = []

        for j in range (0,n-1):
            p = maxSum-k[j]
            q = maxSum-sum

            flag =0
            while (flag == 0):
                r = int(random.uniform(1,q+1))
                if (r + k[j] <= maxSum):
                    flag = 1

            L.append(r)
            k[j]=k[j]+r
            sum=sum+r


        L.append(maxSum-sum)

        M.append(L)


    print (M)
magicSquare()
