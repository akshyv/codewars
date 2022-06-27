# %%
# my solution


def invert(lst):
    if len(lst) == 0:
        return []
    else:
        list = []
        for i in lst:
            list.append(-i)
        return list
# %%
# solution 1


def invert(lst):
    return [-x for x in lst]
