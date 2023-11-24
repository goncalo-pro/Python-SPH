from math import sqrt, pi

from const import *
'''
def smothing_kernel(dst) -> float:
    volume = pi * (S_RAD ** 8) / 4
    value = max(0, S_RAD ** 2 - dst ** 2)
    return value ** 3 / volume

def smothing_kernel_gradient(dst) -> float:
    if dst >= S_RAD: 
        return 0
    else:
        f = S_RAD ** 2 - dst ** 2
        scale = -24 / (pi * (S_RAD **8))
        return scale * dst * (f**2)
'''
def smothing_kernel(dst) -> float:
    if dst >= S_RAD:
        return 0
    else:
        volume = pi * (S_RAD ** 4) / 6
        value = (S_RAD - dst) ** 2 / volume
        return value

def smothing_kernel_gradient(dst) -> float:
    if dst >= S_RAD:
        return 0
    else:
        scale = 12 / ((S_RAD ** 4) * pi)
        value = (dst - S_RAD) * scale
        return value

def distance(p1x, p2x, p1y, p2y) -> float:
    value = sqrt((p2x - p1x) ** 2 + (p2y - p1y) ** 2)
    return value
