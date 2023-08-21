from math import floor, ceil
import timeit

#days = {"saturday":0,"sunday":1,"monday":2,"tuesday":3,"wednesday":4,"thursday":5,"friday":6}

def dayOfWeek(d, m, y):
    y, z = y%100, floor(y/100)
    if m == 1 or m == 2:
        m += 12
        y -= 1
    day = (d+floor((2.6)*(m+1))+y+floor(y/4)+floor(z/4)+(5*z))%7
    return floor(day)

def countingSundays(start=1901, end=2001):
    count = 0
    day = 1
    for year in range(start, end):
        for month in range(1, 12+1):
            if dayOfWeek(day, month, year) == 1:
                count += 1
    return count

print(dayOfWeek(25, 6, 2022))