# Create a function returning multiple values 
import math
def area_circum(radius):
    circumference = math.pi * 2 * radius
    area = math.pi * radius * radius
    return (circumference, radius)

a, c = area_circum(4)

print("Area: ", a, "Circumference:", c)
