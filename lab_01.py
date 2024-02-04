def is_year_leap(year):
    if year < 1582:
        return None

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    leap_year = is_year_leap(year)

    if leap_year == None or 1 > month or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year:
        days[1] = 29
    return days[month-1]


def day_of_year(year, month, day):
    counter_days = 0

    dm = days_in_month(year, month)
    if dm == None or dm < day or day < 1:
        return None

    for i in range(1, month):
        counter_days += days_in_month(year, i)
    return counter_days + day


test_years = [2024, 2023, 2024, 2024, 2000, 2024, 2023, 1581, 2024]
test_months = [2, 3, 3, 13, 2, 12, 12, 1, 2]
test_days = [1, 1, 1, 1, 30, 31, 31, 1, 0]
test_results = [32, 60, 61, None, None, 366, 365, None, None]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    da = test_days[i]
    print(f'{yr} {mo} {da}->', end=' ')
    result = day_of_year(yr, mo, da)
    if result == test_results[i]:
        print('OK')
    else:
        print('Failed')
