'''First thing first in oops'''
'''We have to start with class , Class is Blueprint in any program which follow OOPS'''
class Elevator:
    def __init__(self, idle, num_of_floors, direction, cur_floor):  # Instantiate all attributes
        self.num_of_floors = 6              #
        self.cur_floor = cur_floor
        self.direct = direction
        self.idle = idle

    def __str__(self):
        print ("Wellcome to air_lifters")
        return f"{self.num_of_floors}_{self.cur_floor}"

Building = Elevator(0, 0 , "up",2)
print(Building)