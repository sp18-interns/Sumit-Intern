
class Employee: 
    center = "Not known"
    def __init__(self, name, marks, center): 
        self.name = name 
        self.marks = marks 
        self.center = center 


    def printObj(self):
        print(f"The name is {self.name}")
        print(f"The marks is {self.marks}") 
        print(f"The center is {self.center}") 
    
    @staticmethod
    def greet():
        print("good day")


Yash = Employee("Yash", 34, "Delhi")
Sumit = Employee("Sumit", 34, "Kolkata")
Yash.printObj()
Sumit.printObj()
