import calendar
import datetime

yy = 2020
mm = 6

print(calendar.calendar(yy))

print(calendar.month(yy, mm))

current_time = datetime.datetime.now()

print("Time now at india is : ", end="")
print(current_time)
