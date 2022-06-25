# %%
# my solution

import math
from functools import reduce


def grow(arr):
    if len(arr) != 0:
        product = 1
        for i in arr:
            product = product*i
    else:
        product = 0
    return product

# %%
# solution 1


def grow(arr):
    return reduce(lambda x, y: x * y, arr)

# %%
# solution 2


def grow(arr):
    return math.prod(arr)
