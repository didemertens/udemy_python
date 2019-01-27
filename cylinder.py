
class Cylinder:

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        pi = 22/7
        volume = pi * self.radius * self.radius * self.height
        return volume

    def surface_area(self):
        pi = 22/7
        sur_area = ((2*pi*self.radius) * self.height) + ((pi*self.radius**2)*2)
        return sur_area


c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())
