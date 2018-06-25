dd=int(input("Enter date (dd):"))
mm=int(input("Enter month (mm):"))
yy=int(input("Enter year (yyyy):"))

def nextDate(dd,mm,yy):
    #Months with 31 days
    if dd==31 and (mm==1 or mm==3 or mm==5 or mm==7 or mm==9 or mm==11):
        dd=1
        mm=mm+1
    #Months with 30 days
    elif dd==30 and (mm==4 or mm==6 or mm==8 or mm==10):
        dd=1
        mm=mm+1
    #Not 31st as date months
    elif dd==31 and (mm==2 or mm==4 or mm==6 or mm==8 or mm==10):
        print ("invalid date")
    #year increment for after december 31st
    elif dd==31 and mm==12:
        dd=1
        mm=1
        yy=yy+1
    #February
    elif dd==28 and mm==2 and yy%100==0 and yy%400!=0:#not leap
        dd=1
        mm=mm+1
    elif dd==28 and mm==2 and yy%100==0 and yy%400==0:#leap
        dd=dd+1
    elif dd==28 and mm==2 and yy%4==0:#leap
        dd=dd+1
    elif dd==28 and mm==2 and yy%4!=0:#not leap
        dd=1
        mm=mm+1
#29th Feb
    elif dd==29 and mm==2 and (yy%100==0 and yy%400!=0):#not leap, 1700,1900
        print ("invalid date")
    elif dd==29 and mm==2 and yy%4==0:#leap
        dd=1
        mm=mm+1
    elif dd==29 and mm==2 and yy%4!=0:#if not leap
        print ("invalid date")
    elif dd>29 and mm==2:
        print ("invalid date")
    else:
        dd=dd+1
    return (dd,mm,yy)
print(nextDate(dd,mm,yy))
