#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""

import math


def hypotenuse(x, y, z):
    if z == True:
        return math.hypot(x, y)
    elif z == False:
        return math.sqrt(x**2 - y**2)


a = hypotenuse(3, 4, True)
print(a)

b = hypotenuse(13, 5, False)
print(b)
