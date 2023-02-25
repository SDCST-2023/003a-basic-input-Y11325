#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

import math
print("Volume of a Sphere Calculator\n")
data = input("Press the Enter Key to proceed\n")
question = "Input a number for the radius: "
radius = int(input(question))
print("\n")
V = (4/3)*(math.pi)*(math.pow(radius,3))
print(f"The volume of the sphere is {V}\n")