class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.current = current
        self.top = top
        self.bottom = bottom
    def up(self):
        """Makes the elevator go up one floor."""
        if (self.current + 1) > self.top:
            pass
        else:
            self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if (self.current - 1) < self.bottom:
            pass
        else:
            self.current -= 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor <= self.top and floor >= self.bottom:
            self.current = floor
    def __str__(self):
        return "Current floor: {}".format(self.current)

elevator = Elevator(0, 12, 2)
print(elevator)