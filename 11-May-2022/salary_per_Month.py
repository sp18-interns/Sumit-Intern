class Employee:
    da = 10  # in % deerness allowance this is class attribute
    it = 10  # in % deerness allowance this is class attribute
    wage = 1000  # wages per day

    def __init__(self, name, days_worked):
        self.name = name
        self.days_worked = days_worked

    def salary(self):
        if self.days_worked >= 30:
            return f'(OT Included){30 * self.wage + (self.days_worked - 30) * self.wage }'
        else:
            return f' {self.days_worked * self.wage}'

    def deerness_allowance(self):
        return ((self.days_worked * self.wage) // 100) * self.da

    def income_tax(self):
        if (30 * self.wage + (self.days_worked - 30) * self.wage) or (self.days_worked * self.wage) >= 100000:
            return ((40 * self.wage + (self.days_worked - 30) * self.wage * 1.5) // 100) * self.it

    def __str__(self):
        return f'{self.name}, Gross Salary :{self.salary()}, Deerness Allowance  :{self.deerness_allowance()}, Income ' \
               f'Tax: {self.income_tax()}, '  # if i don't use separate {} then error


e1 = Employee("Vishal", 40)
e2 = Employee("Sumit", 25)
print(e1)
print(e2)
print(f'Hi {e1.name} Your DA is {e1.deerness_allowance()}')
print(f'Hi {e1.name} Your IT is {e1.income_tax()}')
print(f'Hi {e1.name} Your DA is {e2.deerness_allowance()}')
print(f'Hi {e2.name} Your IT is {e2.income_tax()}')
