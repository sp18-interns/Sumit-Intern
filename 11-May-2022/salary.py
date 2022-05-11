class Employee:

    def __init__(self, name, hours_worked, wage_hour):
        self.name = name
        self.hours_worked = hours_worked
        self.wage = wage_hour

    def salary(self):
        if self.hours_worked >= 40:
            return (f'Your CTC with OT is {40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5}')
        else:
            return (f'The CTC is {self.hours_worked * self.wage}')

    def da(self):
        return ((self.hours_worked * self.wage) * 2 // 100)

    def __str__(self):
        return f'{self.name}, {self.salary()}, {self.da()}'  # if i don't use seperate {} then error

    def displayDetails(self):
        print("Name:", self.name, " Salary:", self.salary())


class Manager(Employee):
 pass
e1 = Employee("Vishal", 70, 800)
e2 = Employee("Sumit", 100, 400)
print(e1)
print(e2)
print(f'Hi {e1.name} Your DA is {e1.da()}')
print(f'Hi {e2.name} Your DA is {e2.da()}')


#print(f'Details of all employee: {e1} , {e2}')

#
# def tata():
#     return f'hello sumit'
# print (tata())

# class Salary:
#     def __init__(self, ta, da, hra, epf):
#         self.ta = ta
#         self.da = da
#         self.hra = hra
#         self.
