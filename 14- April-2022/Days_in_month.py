month = int(input("enter the month nummber: "))

def days_in_month(month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        return 28
    return 30

print(days_in_month(month))