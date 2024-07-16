import math
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("radius must be positive")
        self.radius = radius

    def area(self):
        assert self.radius > 0, "radius must be positive"
        return math.pi * self.radius ** 2
    
    def get_coefficient(self, coeffcient):
        self.radius *= coeffcient
        return self.radius
