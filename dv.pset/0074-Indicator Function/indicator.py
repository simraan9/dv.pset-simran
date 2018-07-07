print ('Enter your set with a space:')
L= input().split(' ')
s=input("Enter value to search:")
def indicator(A, x):
    if x in A:
        print (1)
    else:
        print (0)

indicator(L,s)
