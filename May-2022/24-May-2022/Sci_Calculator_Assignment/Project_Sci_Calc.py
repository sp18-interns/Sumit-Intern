import math


class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 // self.num2

    def sin_rad(self):
        print("This function is applicable for num1")
        return math.sin(self.num1)

    def cos_rad(self):
        print("This function is applicable for num1")
        return math.cos(self.num1)

    def tan_rad(self):
        print("This function is applicable for num1")
        return math.tan(self.num1)

    def rad_to_deg(self):
        print("This function is applicable for num1")
        return math.degrees(self.num1)

    def deg_to_rad(self):
        print("This function is applicable for num1")
        return math.radians(self.num1)
