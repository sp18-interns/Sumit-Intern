class Employee:
    count = 0

    def __init__(self, name, post, salary):
        self.name = name
        self.post = post
        self.salary = salary
        Employee.count += 1

    def salary(self, hours_worked, wage):
        if hours_worked > 40:
            return 40 * wage + (hours_worked - 40) * wage * 1.5
        else:
            return hours_worked * wage


    def displayCount(self):
        print("There are %d employees" % Employee.count)

    def displayDetails(self):
        print("Name:", self.name, ", Designation:", self.post, ", Salary:", self.salary)


e1 = Employee("John", "Manager", 50, 800)
e1.displayCount()
print("Details of all employee:")
e1.displayDetails()
