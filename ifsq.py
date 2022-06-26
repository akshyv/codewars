# %%
# my cheat solution


import math
from math import sqrt


def is_square(n):
    for i in (0, n+1):  # range cannot be fixed it should be dynamic
        prod = i*i
        if prod == n:
            status = True
            break
        else:
            status = False
    if status == True:
        return True
    else:
        return False
# %%
# my solution


def is_square(n):
    try:
        return (True if sqrt(n).is_integer() else False)
    except:
        return (False)
# %%
# solution 1


def is_square(n):
    return n >= 0 and (n**0.5) % 1 == 0
# %%
# solution 2


def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0
