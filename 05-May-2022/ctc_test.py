from ctc import weeklyPaid
from ctc import getGrossPay

hours_worked = 50
wage = 100

pay = weeklyPaid(hours_worked, wage)

print(f"Total gross pay: Rs.{pay:.2f} ")

annual_salary = 24.5
no_of_pay_peroids = 12
pay = getGrossPay(annual_salary, no_of_pay_peroids)

print(f"Total gross pay: Rs.{pay:.2f} lakhs ")