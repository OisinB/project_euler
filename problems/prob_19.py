#cheating
import datetime as dt

year = 1901
month = 1
d = dt.date(year,month,1)

end = dt.date(2000,12,31)
result = 0

while d < end:
    result += d.weekday() == 6
    month += 1
    if month > 12:
        month = 1
        year += 1
    d = dt.date(year,month,1)

print(result)
