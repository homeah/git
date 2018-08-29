import time
localtime = time.localtime()
months = (0,31,59,90,120,151,181,212,243,273,304,334)
year = localtime[0]
month = localtime[1]
day = localtime[2]
total = months[month-1] + day
leapyear = 0
if year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):
    leapyear = 1
if leapyear == 1 and month>2:
    total += 1
print('今天是一年中的%d天' %total)
