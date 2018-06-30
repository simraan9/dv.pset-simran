'''
Write a function checkPalindrome(x) which finds if the sum of digits of a
number and sum of digits of same number reversed will be same.
Multiply by place value!!!!!!!!!!
'''
x=int(input("Enter number to check palindrome: "))
def reverse(x):
    num=0
    while x>0:
        r=x%10
        num=(num*10)+r
        x=x//10
    return num
def checkPalindrome(x):
    num=0
    while x>0:
        r=x%10
        num=num+r
        x=x//10
    print (num)
print ('Sum of digits:')
checkPalindrome(x)
print ('Sum of digits reversed:')
checkPalindrome(reverse(x))
