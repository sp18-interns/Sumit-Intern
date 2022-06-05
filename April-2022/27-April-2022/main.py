'''First thing first in oops'''
'''We have to start with class , Class is Blueprint in any program which follow OOPS'''
class Elevator:
    def __init__(self, num_of_floors, cur_floor):  # Instantiate all attributes
        self.num_of_floors =            # Instantiate object
        self.cur_floor = cur_floor

    def __str__(self):    # This method is to print object as string
        print ("Wellcome to air_lifters")
        return f"{self.num_of_floors}_{self.cur_floor}"

    def floor_0(self):
        self.floor_0 = "Ground floor"
        return self.floor_0

building = Elevator(0,2)
a = building.floor_0()
print (a)
print(building)