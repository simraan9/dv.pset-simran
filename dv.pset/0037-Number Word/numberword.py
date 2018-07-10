x=int(input('Enter number upto 100:'))
def spellingWordsAUnit(n):
    ones={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',
    7:'seven',8:'eight',9:'nine'}
    word=ones[n]
    return (word)

def spellingWordsUpto99(n):
    tens=n//10
    units=n%10
    word=''
    if tens==0:
        word=spellingWordsAUnit(n)
    if tens==1:
        unitsOfTen={0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',
        5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}
        word=unitsOfTen[units]
    if tens==2:
        word='twenty '+spellingWordsAUnit(units)
    elif tens==3:
        word='thirty '+spellingWordsAUnit(units)
    elif tens==4:
        word='forty '+spellingWordsAUnit(units)
    elif tens==5:
        word='fifty '+spellingWordsAUnit(units)
    elif tens==6:
        word='sixty '+spellingWordsAUnit(units)
    elif tens==7:
        word='seventy '+spellingWordsAUnit(units)
    elif tens==8:
        word='eighty '+spellingWordsAUnit(units)
    elif tens==9:
        word='ninety '+spellingWordsAUnit(units)
    return (word)
spellingWordsUpto99(x)

def spellingWordsTill1000(n):
