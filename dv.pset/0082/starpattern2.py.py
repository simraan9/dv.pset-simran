a=int(input("Give me a number: "))

def starPattern():
    for i in range(0,a,1):
        for j in range(0,i,1):
            print ('*', end="")
        print('')
    for i in range(a,0,-1):
        for j in range(i,0,-1):
            print ('*', end="")
        print('')
starPattern()
