#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math
print("\nSurface Area of a Cone Calculator\n")
data = input("Press the Enter Key to proceed\n")
_r = "radius: "
_h = "height: "
value_r = int(input(_r))
value_h = int(input(_h))
print("\n")
print(f"radius = {value_r}\nheight = {value_h}")
slant = math.sqrt(math.pow(value_r,2)+math.pow(value_h,2))
print(f"slant height = {slant}")
SA = math.pi * math.pow(value_r,2) + math.pi * value_r * slant
print(f"\nSurface Area = {SA}\n")