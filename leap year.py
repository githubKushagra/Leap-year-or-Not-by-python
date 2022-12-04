# check-that given year is a leap year or not

yr=int(input("enter a year: "))         # enter a year

if yr%100==0:                           # conditions for leap year
    if yr%400==0:
        leap=True
    else:
        leap=False
elif yr%4==0:
    leap=True
else:
    leap=False    
if leap==True:
    print(yr,"is a leap year")
else:
    print(yr,"is not a leap year")
