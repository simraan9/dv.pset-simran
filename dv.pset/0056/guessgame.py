import random
i=int(random.random()*100)
count =0
print("Guess what number i'm guessing ")
g=int(input("What's your guess?"))
while (i!=g):
    if g>i:
        print("Your number is high")
    elif g<i:
        print("Your number is low")
    count=count+1
    g=int(input("What's your guess?"))
if g==i:
    print("You win!")
print ("Your number of attempts: "+str(count))
