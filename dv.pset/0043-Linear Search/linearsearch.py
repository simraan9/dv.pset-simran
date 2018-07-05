print ('Enter your list items with a space:')
A= input().split(' ')
s=input("Enter value to search:")

def linearSearch(L):
    for i in range (0,len(L)):
        if s==L[i]:
            print (s,'is the ',i,'item')

linearSearch(A)
