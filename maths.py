from math import sqrt, pi

from const import *

'''
MATH FUCNTION FOR CALCULATION OF INFLUENCE IN DENSITY WITH DISTANCE
'''
def smothing_kernel(dst) -> float:
    if dst >= S_RAD:
        return 0
    else:
        volume = pi * (S_RAD ** 4) / 6
        value = (S_RAD - dst) ** 2 / volume
        return value

'''
DERIVATIVE OF THE PREVIOUS FUNCTION
'''
def smothing_kernel_gradient(dst) -> float:
    if dst >= S_RAD:
        return 0
    else:
        scale = 12 / ((S_RAD ** 4) * pi)
        value = (dst - S_RAD) * scale
        return value

'''
MATH FUNCTION TO CALCULATE DISTANCE BETWEEN TWO POINTS
'''
def distance(p1x, p2x, p1y, p2y) -> float:
    value = sqrt((p2x - p1x) ** 2 + (p2y - p1y) ** 2)
    return value
