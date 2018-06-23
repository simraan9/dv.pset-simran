a=int(input("Enter length of side 1:"))
b=int(input("Enter length of side 2:"))
c=int(input("Enter length of side 3:"))

if (a**2)+(b**2)==(c**2) or (b**2)+(c**2)==a**2 or (a**2)+(c**2)==b**2:
    print ("True")
else:
    print ("False")
