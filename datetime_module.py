import datetime

t = datetime.time(5,25,1)
print(t)
t.minute

print(datetime.time.min)
print(datetime.time.max)


today = datetime.date.today()
print(today)

print(today.timetuple())

d1 = datetime.date(2015,3,11)
print(d1)

d2 = d1.replace(year=1990)
print(d2)

print(d1-d2)
