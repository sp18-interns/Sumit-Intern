"""This is Basic Salary Calculator Program using the concept of OOP & Python"""
from _datetime import datetime


class Payroll:  # 'class is for class definition',  'Employee is name of class'
    da = 10  # in % dearness allowance this is class attribute
    it = 10  # in % dearness allowance this is class attribute

    def __init__(self, name, hours_worked, wage_hour, designation):
        """
        @'name, hours_worked, wage_hour' what data initialize  an Employee object
        """
        self._name = name
        self.hours_worked = hours_worked
        self.wage = wage_hour
        self.designation = designation

        """
        Three data attribute for every employee object
        @self.name = name
        @self.hours_worked = hours_worked
        @self.wage = wage_hour 
        """

    def salary(self):
        """
        @salary(self) : salary method to initialize the formula of salary calculation
        """
        if self.hours_worked > 50:
            """
            @ Dot notation (self.wage, self.hour_worked ) is used to access the data
            """
            return 50 * self.wage + (self.hours_worked - 50) * self.wage * 1.50
        else:
            return self.hours_worked * self.wage

    def dearness_allowance(self):
        """
        @dearness_allowance(self) : dearness_allowance method to initialize the formula of DA calculation
        """
        return ((self.hours_worked * self.wage) // 100) * self.da

    def income_tax(self):
        """
        @income_tax(self) : income_tax method to initialize the formula of it calculation
        """
        if (50 * self.wage + (self.hours_worked - 50) * self.wage * 1.5) or (self.hours_worked * self.wage) >= 100000:
            return ((50 * self.wage + (self.hours_worked - 50) * self.wage * 1.5) // 100) * self.it

    def __str__(self):
        return f'{self._name}, Gross Salary : {self.salary()}, Dearness Allowance  : {self.dearness_allowance()}, Income ' \
               f'Tax: {self.income_tax()}, '  # if i don't use separate {} then error

    @property
    def name(self):
        return self._name


class Bonus_salary(Payroll):

    def salary(self):
        if self.hours_worked >= 100:
            """
            @ Dot notation (self.wage, self.hour_worked ) is used to access the data
            """
            return 100 * self.wage + (self.hours_worked - 100) * self.wage * 2


class Salary_slip(Bonus_salary):
    def print_salary_slip(self):
        return f''' To {self._name}
                     {self.designation}   
                    Hello {self._name} this month your Gross salary is {self.salary()}
                    
                                                                Finance Department
                                                                {datetime.now()}
                '''
