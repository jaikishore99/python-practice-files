# imports calender

import calendar

# imports time and date

import datetime

# current year

currentyear = 2020

# current month

currentmonth = 6

# prints complete year with 12 mnts

print("current year" + calendar.calendar(currentyear))

# prints selectes month

print("current month" + calendar.month(currentyear, currentmonth))

# prints date and time

current_time = datetime.datetime.now()

# prints current date and time
print("Time now at india is : current date / time = ", end=" ")

# gets the output in the code given

print(current_time)
