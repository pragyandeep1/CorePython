import datetime
from datetime import date
from time import time

datetime_object = datetime.datetime.now()
print(datetime_object)

d = datetime.date(2019, 4, 13)
print(d)
today = date.today()

print("Current date =", today)

date_object = datetime.date.today()
print(date_object)
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time()
print("b =", b)

# time(hour, minute and second)
c = time()
print("c =", c)

# time(hour, minute, second, microsecond)
d = time()
print("d =", d)


a = date.today()
print("year =", a.year)
print("month =", a.month)
#print("hour =", a.hour)
#print("minute =", a.minute)
#print("timestamp =", a.timestamp())





