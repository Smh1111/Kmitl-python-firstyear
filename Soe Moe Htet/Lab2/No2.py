import math

radius = float(input("Enter the radius: "))
length = float(input("Enter the length: "))

area = math.pi * radius * radius
volume = area * length

print("area = ", area)
print("volume = ", volume)