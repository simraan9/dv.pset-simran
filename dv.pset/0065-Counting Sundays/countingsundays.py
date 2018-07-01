def nextDate(L):
    #Months with 31 days
    if L[0]==31 and (L[1]==1 or L[1]==3 or L[1]==5 or L[1]==7 or L[1]==8 or L[1]==10):
        L[0]=1
        L[1]=L[1]+1
    #Months with 30 days
    elif L[0]==30 and (L[1]==4 or L[1]==6 or L[1]==9 or L[1]==11):
        L[0]=1
        L[1]=L[1]+1
    #Not 31st as date months
    elif L[0]==31 and (L[1]==2 or L[1]==4 or L[1]==6 or L[1]==8 or L[1]==10):
        print ("invalid date")
    #year increment for after december 31st
    elif L[0]==31 and L[1]==12:
        L[0]=1
        L[1]=1
        L[2]=L[2]+1
    #February
    elif L[0]==28 and L[1]==2 and L[2]%100==0 and L[2]%400!=0:#not leap
        L[0]=1
        L[1]=L[1]+1
    elif L[0]==28 and L[1]==2 and L[2]%100==0 and L[2]%400==0:#leap
        L[0]=L[0]+1
    elif L[0]==28 and L[1]==2 and L[2]%4==0:#leap
        L[0]=L[0]+1
    elif L[0]==28 and L[1]==2 and L[2]%4!=0:#not leap
        L[0]=1
        L[1]=L[1]+1
#29th Feb
    elif L[0]==29 and L[1]==2 and (L[2]%100==0 and L[2]%400!=0):#not leap, 1700,1900
        print ("invalid date")
    elif L[0]==29 and L[1]==2 and L[2]%4==0:#leap
        L[0]=1
        L[1]=L[1]+1
    elif L[0]==29 and L[1]==2 and L[2]%4!=0:#if not leap
        print ("invalid date")
    elif L[0]>29 and L[1]==2:
        print ("invalid date")
    else:
        L[0]=L[0]+1
    return (L)

def countingSundays():
    count=1 #Monday, 1st Jan 1900
    M=[1,1,1900]
    sun=0
    while M[2]<2001:
        next=nextDate(M)
        count=count+1
        if M[0]==1 and count%7==0:
                sun=sun+1
    print (sun,'sundays')
countingSundays()
