'''First thing first in oops'''

'''We have to start with class , Class is Blueprint in any program which follow OOPS'''


class Elevator:
    def __init__(self, num_of_floors, cur_floor, floor_0,):  # Instantiate all attributes
        self.floor_0 = None
        self.floor_1 = None
        self.floor_2 = None
        self.floor_3 = None
        self.num_of_floors = 4  # Instantiate object
        self.cur_floor = cur_floor

    def __str__(self):  # This method is to print object as string
        print("Wellcome to air_lifters")
        return f"{self.num_of_floors}_{self.cur_floor} "

    def direction(self):
        if self.direction == "up":
            return "up"
        else:
            return "down"

    def floor_0(self):
        self.floor_0 = "Ground floor"
        return self.floor_0

    def floor_1(self):
        self.floor_1 = "First Floor"
        return self.floor_1

    def floor_2(self):
        self.floor_2 = "Second  floor"
        return self.floor_2

    def floor_3(self):
        self.floor_3 = "Third floor"
        return self.floor_3


building = Elevator(0,0 ,2)
building.direction()
a = building.floor_0()
print(a)
print(building)
print(building.direction('up'))