class Employee:
    da = 10  # in % deerness allowance this is class attribute
    it = 10  # in % deerness allowance this is class attribute

    def __init__(self, name, hours_worked, wage_hour):
        self.name = name
        self.hours_worked = hours_worked
        self.wage = wage_hour

    def salary(self):
        if self.hours_worked >= 40:
            return f'(OT Included){40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5}'
        else:
            return f' {self.hours_worked * self.wage}'

    def deerness_allowance(self):
        return ((self.hours_worked * self.wage) // 100) * self.da

    def income_tax(self):
        if (40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5) or (self.hours_worked * self.wage) >= 100000:
            return ((40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5) // 100) * self.it

    def __str__(self):
        return f'{self.name}, Gross Salary :{self.salary()}, Deerness Allowance  :{self.deerness_allowance()}, Income ' \
               f'Tax: {self.income_tax()}, '  # if i don't use separate {} then error


e1 = Employee("Vishal", 41, 2000)
e2 = Employee("Sumit", 39, 2000)
print(e1)
print(e2)
print(f'Hi {e1.name} Your DA is {e1.deerness_allowance()}')
print(f'Hi {e2.name} Your DA is {e2.deerness_allowance()}')
