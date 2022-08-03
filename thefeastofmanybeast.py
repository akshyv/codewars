# check if first and last letters of beast and food is same
# %%
# my sol
def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    return False
# %%
# sol 1


def feast(beast, dish):
    return beast[0] == dish[0] and dish[-1] == beast[-1]
