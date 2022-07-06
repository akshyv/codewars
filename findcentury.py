# find the century of year
# %%
# sol 1


import math


def century(year):
    if year <= 100:
        return 1
    else:
        if year % 100 == 0:
            return(int(year/100))
        else:
            return(int(year/100)+1)
# %%
# sol 1


def century(year):
    return (year + 99) // 100
# %%
# sol 2


def century(year):
    return math.ceil(year / 100)
# %%
# sol 3


def century(year):
    return (year / 100) if year % 100 == 0 else year // 100 + 1
# %%
# sol 4


def century(year):
    return (year - 1) // 100 + 1
