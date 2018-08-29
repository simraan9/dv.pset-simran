#x=int(input('Enter number upto 1000:'))
word=''
def spellingWordsAUnit(n):
    ones={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',
    7:'seven',8:'eight',9:'nine'}
    word=ones[n]
    return (word)

def spellingWordsUpto99(n):
    tens=n//10
    units=n%10
    global word
    if tens==0:
        word=spellingWordsAUnit(n)
    if tens==1:
        unitsOfTen={0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',
        5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}
        word=unitsOfTen[units]
    if tens==2:
        word='twenty'+spellingWordsAUnit(units)
    elif tens==3:
        word='thirty'+spellingWordsAUnit(units)
    elif tens==4:
        word='forty'+spellingWordsAUnit(units)
    elif tens==5:
        word='fifty'+spellingWordsAUnit(units)
    elif tens==6:
        word='sixty'+spellingWordsAUnit(units)
    elif tens==7:
        word='seventy'+spellingWordsAUnit(units)
    elif tens==8:
        word='eighty'+spellingWordsAUnit(units)
    elif tens==9:
        word='ninety'+spellingWordsAUnit(units)
    return (word)

def spellingWordsTill999(n):
    hundreds=n//100
    tens=n%100
    global word
    if hundreds==0:
        word=spellingWordsUpto99(n)
    if hundreds==1:
        word='onehundred'+spellingWordsUpto99(tens)
    if hundreds==2:
        word='twohundred'+spellingWordsUpto99(tens)
    elif hundreds==3:
        word='threehundred'+spellingWordsUpto99(tens)
    elif hundreds==4:
        word='fourhundred'+spellingWordsUpto99(tens)
    elif hundreds==5:
        word='fivehundred'+spellingWordsUpto99(tens)
    elif hundreds==6:
        word='sixhundred'+spellingWordsUpto99(tens)
    elif hundreds==7:
        word='sevenhundred'+spellingWordsUpto99(tens)
    elif hundreds==8:
        word='eighthundred'+spellingWordsUpto99(tens)
    elif hundreds==9:
        word='ninehundred'+spellingWordsUpto99(tens)
    elif n==1000:
        word='onethousand'
    return word
#print (spellingWordsTill999(x))

def counter(returnedWord,n):
    count=len(returnedWord)
    if n>100 and n%100!=0:
        count=count+3
    return count
#print(counter(word,x))

def countTill1000():
    sum=0
    for i in range (1,1001):
        sum=sum+ int(counter(spellingWordsTill999(i),i))
    return sum
print ('sum of letters 1-1000=',countTill1000())
