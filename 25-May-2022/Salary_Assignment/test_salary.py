# class Employee:
#     da = 10  # in % deerness allowance this is class attribute
#     it = 10  # in % deerness allowance this is class attribute
#
#     def __init__(self, name, hours_worked, wage_hour):
#         self.name = name
#         self.hours_worked = hours_worked
#         self.wage = wage_hour
#
#     def salary(self):
#         if self.hours_worked >= 50:
#             return f'(OT Included){40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5}'
#         else:
#             return f' {self.hours_worked * self.wage}'
#
#     def deerness_allowance(self):
#         return ((self.hours_worked * self.wage) // 100) * self.da
#
#     def income_tax(self):
#         if (40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5) or (self.hours_worked * self.wage) >= 100000:
#             return ((40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5) // 100) * self.it
#
#     def __str__(self):
#         return f'{self.name}, Gross Salary :{self.salary()}, Deerness Allowance  :{self.deerness_allowance()}, Income ' \
#                f'Tax: {self.income_tax()}, '  # if i don't use separate {} then error
# from salary_per_hour import Employee
from salary_per_hour import Employee as EmployeePerHour


# class Employee:
#     da = 10  # in % deerness allowance this is class attribute
#     it = 10  # in % deerness allowance this is class attribute
#     wage = 1000  # wages per day
#
#     def __init__(self, name, days_worked):
#         self.name = name
#         self.days_worked = days_worked
#
#     def salary(self):
#         if self.days_worked >= 30:
#             return f'(OT Included){30 * self.wage + (self.days_worked - 30) * self.wage }'
#         else:
#             return f' {self.days_worked * self.wage}'
#
#     def deerness_allowance(self):
#         return ((self.days_worked * self.wage) // 100) * self.da
#
#     def income_tax(self):
#         if (30 * self.wage + (self.days_worked - 30) * self.wage) or (self.days_worked * self.wage) >= 100000:
#             return ((40 * self.wage + (self.days_worked - 30) * self.wage * 1.5) // 100) * self.it
#
#     def __str__(self):
#         return f'{self.name}, Gross Salary :{self.salary()}, Deerness Allowance  :{self.deerness_allowance()}, Income ' \
#                f'Tax: {self.income_tax()}, '  # if i don't use separate {} then error
# from salary_per_Month import Employee
from salary_per_Month import Employee as EmployeePerMonth


if __name__ == '__main__':
    e1 = EmployeePerHour("Vrushali", 51, 2000)
    e2 = EmployeePerHour("Sushma", 50, 2000)
    print(e1)
    print(e2)
    e1_sallary = e1.salary()
    e1_da = e1.dearness_allowance()
    e1_it = e1.income_tax()
    e2_sallary = e2.salary()
    e2_da = e2.dearness_allowance()
    e2_it = e2.income_tax()

    print(f'{e1.name}. Your Net Salary is {(e1_sallary + e1_da) - e1_it}')
    print(f'{e2.name}. Your Net Salary is {(e2_sallary + e2_da) - e2_it}')
