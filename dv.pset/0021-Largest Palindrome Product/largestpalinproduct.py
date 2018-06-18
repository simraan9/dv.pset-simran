'''
The largest palindrome made from the product of two 2-digit numbers is 9009=91×99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
#x=int(input("Enter no. to reverse:"))
def reverse(x):
    num=0
    while x>0:
        r=x%10
        num=(num*10)+r
        x=x//10
    return num
    #print ('Reverse: ',num)

def ThreeDigProduct():
    m=0
    max=0
    for i in range (999,99,-1):
        for j in range (i,99,-1):
            product=i*j
            if product==reverse(product):
                m=product
                if m>max:
                    max=m
                    print (i,'*',j,'=',max)
ThreeDigProduct()
