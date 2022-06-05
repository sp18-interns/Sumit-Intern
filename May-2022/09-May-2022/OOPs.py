# # Create a new object type called Sample
# class Sample:
#     pass
#
# # Instance of Sample
# x = Sample()
#
# print(type(x))
species = 'mamilia'

class Dog:
    # Class Object Attribute
    species = 'mammal'
    colour = 'black'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
sam = Dog('Laby', "tata")
pam = Dog('Pug','Pam')
#dog = Dog()
print(sam.name)
print(sam.breed)
print(sam.colour)
print(pam.name)
print(pam.breed)
print(pam.colour)
print(pam.species)