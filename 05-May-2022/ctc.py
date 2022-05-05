
def weeklyPaid(hours_worked, wage):
    if hours_worked > 40:
        return 40 * wage + (hours_worked - 40) * wage * 1.5
    elif hours_worked < 100:
        return
    else:
        return hours_worked * wage

def getGrossPay(annual_salary, no_of_pay_peroids):
    return float(annual_salary / no_of_pay_peroids)