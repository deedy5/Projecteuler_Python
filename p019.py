##Euler 19

start = '01, 01, 1901'
finish = '31, 12, 2000'
start_day = 'monday'

def is_leap(year):
    if str(year)[2:] == '00':
        if year % 400 == 0:
            return True
    elif year % 4 == 0:
        return True

def days_in_month(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap(year):
            return 29
        else:
            return 28
    else:
        return 31

s_d, s_m, s_y = [int(i.strip()) for i in start.split(',')]
f_d, f_m, f_y = [int(i.strip()) for i in finish.split(',')]

count_sunday = 0
count_days = 0

for year in range(s_y, f_y + 1):
    for month in range(1, 13):
        days_in_m = days_in_month(year, month)
        for day in range(1, days_in_m + 1,):
            count_days += 1
            if day == 1 and (count_days+6)%7 == 0:
                count_sunday += 1

print(f'{count_sunday = }')




        

