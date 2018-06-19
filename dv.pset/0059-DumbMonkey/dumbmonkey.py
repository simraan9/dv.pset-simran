a=int(input("Enter pillar length:"))
def dumbMonkey(x):
    while x>3:
        if x%2==0:
            print ("NO")
            break
        else:
            print ("YES")
            break
    if x<=3:
        print ("Monkey falls over the pillar")
dumbMonkey(a)
