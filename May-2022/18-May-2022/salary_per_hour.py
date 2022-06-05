class Employee:
    da = 10  # in % deerness allowance this is class attribute
    it = 10  # in % deerness allowance this is class attribute

    def __init__(self, name, hours_worked, wage_hour):
        self.name = name
        self.hours_worked = hours_worked
        self.wage = wage_hour

    def salary(self):
        if self.hours_worked >= 50:
            return f'OT{40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5}'
        else:
            return f'{self.hours_worked * self.wage}'   # problem is here with f' { }' this space after inverted comma

    def deerness_allowance(self):
        return ((self.hours_worked * self.wage) // 100) * self.da

    def income_tax(self):
        if (40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5) or (self.hours_worked * self.wage) >= 100000:
            return ((40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5) // 100) * self.it

    def __str__(self):
        return f'{self.name}, Gross Salary :{self.salary()}, Deerness Allowance  :{self.deerness_allowance()}, Income ' \
               f'Tax: {self.income_tax()}, '  # if i don't use separate {} then error
