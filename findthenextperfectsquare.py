# if a number is perfect squre number then return (sqrt+1)**2 else -1
# %%
# sol 1
import math


def find_next_square(sq):
    if(sq >= 0):
        root = int(math.sqrt(sq))
        if ((root*root) == sq):
            return ((root+1)*(root+1))
        return (-1)
# %%
# sol 1


def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
