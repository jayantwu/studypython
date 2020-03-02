def is_leapyear(year):
    return  year % 4 == 0 and year % 100 != 0 or year % 400 ==  0

def which_day(year, month, day):

    months = [
            [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            ][is_leapyear(year)]
    days = 0
    for index in range(month - 1):
        days += months[index]
    return days + day
    """
    month1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    if is_leapyear(year):
        if month == 1:
            days = day
        else:
            days = sum(month2[:month-1]) + day
    else:
        if month == 1:
            days = day
        else:
            days = sum(month1[:month-1]) + day
    return days
    """

print(which_day(2020, 3, 2))



