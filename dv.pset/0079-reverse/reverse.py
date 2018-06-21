x=int(input("Enter no to reverse:"))
def reverse(x):
    num=0
    while x>0:
        r=x%10
        num=(num*10)+r
        x=x//10
    print ('Reverse: ',num)
reverse(x)
