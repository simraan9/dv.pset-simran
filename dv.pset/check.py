x=int(input('Enter number upto 1000:'))
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
#spellingWordsUpto99(x)

def spellingWordsTill999(n):
    hundreds=n//100
    tens=n%100
    word=''
    if hundreds==0:
        word=spellingWordsUpto99(n)
    if hundreds==1:
        word='one hundred '+spellingWordsUpto99(tens)
    if hundreds==2:
        word='two hundred '+spellingWordsUpto99(tens)
    elif hundreds==3:
        word='three hundred '+spellingWordsUpto99(tens)
    elif hundreds==4:
        word='four hundred '+spellingWordsUpto99(tens)
    elif hundreds==5:
        word='five hundred '+spellingWordsUpto99(tens)
    elif hundreds==6:
        word='six hundred '+spellingWordsUpto99(tens)
    elif hundreds==7:
        word='seven hundred '+spellingWordsUpto99(tens)
    elif hundreds==8:
        word='eight hundred  '+spellingWordsUpto99(tens)
    elif hundreds==9:
        word='nine hundred '+spellingWordsUpto99(tens)
    return word
#print (spellingWordsUpto99(x))

def spellingWordsUpto9999(n):
    thousand=n//1000
    hundreds=n%1000
    word=''
    if thousand==0:
        word=spellingWordsTill999(n)
    if thousand==1:
        word='one thousand '+spellingWordsTill999(hundreds)
    if thousand==2:
        word='two thousand '+spellingWordsTill999(hundreds)
    elif thousand==3:
        word='three thousand '+spellingWordsTill999(hundreds)
    elif thousand==4:
        word='four thousand '+spellingWordsTill999(hundreds)
    elif thousand==5:
        word='five thousand '+spellingWordsTill999(hundreds)
    elif thousand==6:
        word='six thousand '+spellingWordsTill999(hundreds)
    elif thousand==7:
        word='seven thousand '+spellingWordsTill999(hundreds)
    elif thousand==8:
        word='eight thousand  '+spellingWordsTill999(hundreds)
    elif thousand==9:
        word='nine thousand '+spellingWordsTill999(hundreds)
    return word

def wordsTill99999(n):
    tenTh=n//10000
    thousand=n%10000
    word=''

    if tenTh==0:
        word=spellingWordsUpto9999(n)
    if tenTh==1:
        unitsOfTenTh={0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',
        5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}
        word=unitsOfTenTh[thousand//1000] + ' thousand '+spellingWordsTill999(n%1000)
    if tenTh==2:
        unitsOfTen={0:'',1:'one',2:'two',3:'three',4:'four',
        5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        word='twenty '+ unitsOfTen[thousand//1000] +' thousand'+spellingWordsTill999(n%1000)
    elif tenTh==3:
        unitsOfTen={0:'',1:'one',2:'two',3:'three',4:'four',
        5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        word='thirty '+ unitsOfTen[thousand//1000] +' thousand'+spellingWordsTill999(n%1000)
    elif tenTh==4:
        unitsOfTen={0:'',1:'one',2:'two',3:'three',4:'four',
        5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        word='forty '+ unitsOfTen[thousand//1000] +' thousand'+spellingWordsTill999(n%1000)
    elif tenTh==5:
        unitsOfTen={0:'',1:'one',2:'two',3:'three',4:'four',
        5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        word='fifty '+ unitsOfTen[thousand//1000] +' thousand'+spellingWordsTill999(n%1000)
    elif tenTh==6:
        unitsOfTen={0:'',1:'one',2:'two',3:'three',4:'four',
        5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        word='sixty '+ unitsOfTen[thousand//1000] +' thousand'+spellingWordsTill999(n%1000)
    elif tenTh==7:
        unitsOfTen={0:'',1:'one',2:'two',3:'three',4:'four',
        5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        word='seventy '+ unitsOfTen[thousand//1000] +' thousand'+spellingWordsTill999(n%1000)
    elif tenTh==8:
        unitsOfTen={0:'',1:'one',2:'two',3:'three',4:'four',
        5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        word='eighty '+ unitsOfTen[thousand//1000] +' thousand'+spellingWordsTill999(n%1000)
    elif tenTh==9:
        unitsOfTen={0:'',1:'one',2:'two',3:'three',4:'four',
        5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        word='ninety '+ unitsOfTen[thousand//1000] +' thousand'+spellingWordsTill999(n%1000)
    return word
print (wordsTill99999(x))
