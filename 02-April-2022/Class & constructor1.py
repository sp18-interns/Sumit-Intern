

class Sparkeighteen:

    def __init__(self, City_1, City_2):
        self.City_1 = City_1
        self.City_2 = City_2
    
        

    def config(self):
        print("The company is located in : ", self.City_1, self.City_2)

company1 = Sparkeighteen('PUNE',"")
company2 = Sparkeighteen('Delhi',"")




company1.config()
company2.config()
