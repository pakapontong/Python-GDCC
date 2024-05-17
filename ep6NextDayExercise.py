year = int(input("Enter year : "))
leap_year = False
if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True

max_day = 30
month = int(input("Enter Month : "))
if month in (1,3,5,7,8,10,12):
    max_day = 31
elif month == 2:
    if leap_year:
        max_day = 29
    else:
        max_day = 28

day = int(input("Enter Day : "))
if day < max_day:
    day = day + 1
elif day == max_day:
    day = 1
    if month == 12:
        month = 1
        year = year + 1 
    else:
        month = month + 1
else:
    print("Date invalid")

print("The Next Date is {}-{}-{}".format(day,month,year))
