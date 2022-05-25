"""This is Basic Salary Calculator Program using the concept of OOP & Python"""


class Employee:  # 'class is for class definition',  'Employee is name of class'
    da = 10  # in % dearness allowance this is class attribute
    it = 10  # in % dearness allowance this is class attribute

    def __init__(self, name, hours_worked, wage_hour):  # __init__ is for special method to create instance
        """
        @__init__ is for special method to create instance
        @'self' is for parameter is for instance for class
        @'name, hours_worked, wage_hour' what data initialize  an Employee object
        """
        self.name = name
        self.hours_worked = hours_worked
        self.wage = wage_hour

        """
        Three data attribute for every employee object
        @self.name = name
        @self.hours_worked = hours_worked
        @self.wage = wage_hour 
        """

    def salary(self):
        """
        @salary(self) : salary method to initialize the formula of salary calculation
        self is used to refer and instance
        """
        if self.hours_worked >= 50:
            """
            @ Dot notation (self.wage, self.hour_worked ) is used to access the data
            """
            return 40 * self.wage + (self.hours_worked - 40) * self.wage * 1.50
        else:
            return self.hours_worked * self.wage

    def dearness_allowance(self):
        """
        @dearness_allowance(self) : dearness_allowance method to initialize the formula of DA calculation
        self is used to refer and instance
        """
        return ((self.hours_worked * self.wage) // 100) * self.da

    def income_tax(self):
        """
        @income_tax(self) : income_tax method to initialize the formula of it calculation
        self is used to refer and instance
        """
        if (40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5) or (self.hours_worked * self.wage) >= 100000:
            return ((40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5) // 100) * self.it

    def __str__(self):
        return f'{self.name}, Gross Salary : {self.salary()}, Dearness Allowance  : {self.dearness_allowance()}, Income ' \
               f'Tax: {self.income_tax()}, '  # if i don't use separate {} then error
        """
        __str__ is the special method to return the string
        """
