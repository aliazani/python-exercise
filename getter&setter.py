class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2


small_one = Circle(10)
small_one.radius = 20
print(small_one.diameter)
print(small_one.radius)
print(small_one.diameter)
