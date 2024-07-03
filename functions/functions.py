def is_year_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if year < 1582 or month < 1 or 12 < month:
        return None
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days_in_months[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    if day < 1 or 31 < day:
        return None
    
    month30 = [4, 6, 9, 11]
    month31 = [1, 3, 5, 7, 8, 10, 12]
    if month in month31:
        if day > 31:
            return None
    elif month in month30:
        if day > 30:
            return None
    elif month == 2:
        if is_year_leap(year) and day > 29:
            return None
        elif not is_year_leap(year) and day > 28:
            return None
    
    quantity_days = 0
    for i in range(month):
        i += 1
        quantity_days += days_in_month(year, i)

    if month in month31:
        quantity_days = quantity_days - 31 + day
        return quantity_days
    elif month in month30:
        quantity_days = quantity_days - 30 + day
        return quantity_days
    elif month == 2:
        if is_year_leap(year):
            quantity_days = quantity_days - 29 + day
            return quantity_days            
        else:
            quantity_days = quantity_days - 28 + day
            return quantity_days
    
print(day_of_year(2024, 12, 31))
print(day_of_year(2024, 11, 30))
print(day_of_year(2024, 10, 31))
print(day_of_year(2024, 9, 30))
print(day_of_year(2024, 8, 31))
print(day_of_year(2024, 7, 31))
print(day_of_year(2024, 6, 30))
print(day_of_year(2024, 5, 31))
print(day_of_year(2024, 4, 30))
print(day_of_year(2024, 3, 31))
print(day_of_year(2024, 2, 29))
print(day_of_year(2024, 1, 31))