''' 
# Bai 6.7
@author: packkkk
'''

from datetime import datetime
import calendar
day = int(input("Input day: "))
month = int(input("Input month: "))
year = int(input("Input year: "))
datetime_str = datetime(year, month, day)
print("Datetime: ", datetime_str.strftime("%d - %m - %Y") )
print ('%d is a leap year' % year) if calendar.isleap(year) else print ('%d is not a leap year' % year)

weekday = calendar.weekday(year, month, day)
day_of_the_week = ""
if weekday==0 :
    day_of_the_week = "Monday"
elif weekday ==1:
    day_of_the_week = "Tuesday"
elif weekday ==2:
    day_of_the_week = "Wednesday"
elif weekday ==3:
    day_of_the_week = "Thursday"
elif weekday ==4:
    day_of_the_week = "Friday"
elif weekday ==5:
    day_of_the_week = "Saturday"
else:
    day_of_the_week = "Sunday"
print("The date %d/%d/%d is a %s" %(day, month, year, day_of_the_week))
number_of_days = calendar.monthrange(year, month)[1]
print("Number of day in ", month, " is ", number_of_days )
