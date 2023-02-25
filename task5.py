#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.

import math 
print("\nFind radius of a sphere with given volume --- Calculator")
data = input("\nPress the Enter Key to proceed\n\n")
print(111*"*")
_V = "\n\nVolume: "
Volume = float(input(_V))
r_3 = Volume/(4/3)/math.pi
r = r_3 ** (1/3)
print("\n\n")
print(111*"=")
print(f"\n\nradius = {r}\n\n\n")