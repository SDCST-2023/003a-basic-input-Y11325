#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

import math
print("ax + b = c  calculator\n")
data = input("Press the Enter Key to proceed\n")
_a = "value of a: "
_b = "value of b: "
_c = "value of c: "
value_a = int(input(_a))
value_b = int(input(_b))
value_c = int(input(_c))
print("\n")
print(f"step 1: {value_a}x = {value_c} - {value_b}")
value_step1 = value_c - value_b
print(f"step 2: x = {value_step1}/{value_a}")
end_number = value_step1/value_a
print(f"step 3: x = {end_number}\n")