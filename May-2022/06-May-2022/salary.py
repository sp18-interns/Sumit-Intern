class Employee:
    def __init__(self, name, post, hours_worked, wage_hour):
        self.name = name
        self.post = post
        self.hours_worked = hours_worked
        self.wage = wage_hour

    def salary(self):
        if self.hours_worked > 40:
            return (f'{40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5}')
        else:
            return (f'The CTC is {self.hours_worked * self.wage}')

    def __str__(self):
        return f'{self.name}, {self.post}, {self.salary()}' # if i don't use seperate {} then error

    def displayDetails(self):
        print("Name:", self.name, ", Designation:", self.post, ", Salary:", self.salary())


e1 = Employee("John", "Manager", 50, 800)
print(e1)
print(f'Details of all employee: {e1}')


def tata():
    return f'hello sumit'
print (tata())

# class Salary:
#     def __init__(self, ta, da, hra, epf):
#         self.ta = ta
#         self.da = da
#         self.hra = hra
#         self.