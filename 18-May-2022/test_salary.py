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
    e1 = EmployeePerHour("Vrushali", 49, 2000)
    e2 = EmployeePerHour("Sushma", 39, 2000)
    print(e1)
    print(e2)
    print(f'Hi {e1.name} Your DA is {e1.deerness_allowance()}')
    print(f'Hi {e1.name} Your IT is {e1.income_tax()}')
    print(f'Hi {e1.name} Your DA is {e2.deerness_allowance()}')
    print(f'Hi {e2.name} Your IT is {e2.income_tax()}')
