a=int(input("Give me a number: "))

def starPattern():
    for i in range(a,0,-1):
        for j in range(i,0,-1):
            print ('*', end="")
        print('')
starPattern()
