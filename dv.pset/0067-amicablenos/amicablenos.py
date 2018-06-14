def divisors(n):
    sum=0
    for i in range (1,n,1):
        if n%i==0:
            sum=sum+i
    return sum

def amicableNo():
    sum=0
    for j in range (1,10000,1):
        if divisors(divisors(j))==j:
            sum=sum+j
    print ('Sum of amicable nos under 10,000=',sum)
amicableNo()
