import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

radius = 8
print(f"The volume of the sphere with radius {radius} is: {sphere_volume(radius)}")