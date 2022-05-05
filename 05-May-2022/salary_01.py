class Employee:
    def __init__(self, name, post, hours_worked, wage):
        self.name = name
        self.post = post
        self.hours_worked = hours_worked
        self.wage = wage

    def __str__(self):
        return f'{self.salary()}'

    def salary(self):
        if self.hours_worked > 40:
            return (f'{40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5}')
        else:
            return (f'The CTC is {self.hours_worked * self.wage}')


    def displayDetails(self):
        print("Name:", self.name, ", Designation:", self.post, ", Salary:", self.salary())

e1 = Employee("John", "Manager", 50, 800)
print(e1)
print("Details of all employee:")
e1.displayDetails()
