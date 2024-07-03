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
    quantity_days = 0
    iteracion = 1
    for iteracion in range(month):
        iteracion += 1
        quantity_days += days_in_month(year, iteracion)
        if 
        print(f"iteración: {iteracion}, días contados: {quantity_days}")
    return quantity_days
    
print(day_of_year(2024, 9, 31))
