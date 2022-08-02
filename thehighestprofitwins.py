# take in array and return smallest and largest element as array
# %%
# my sol
def min_max(lst):
    if len(lst) <= 1:
        lst.append(lst[0])   # to send the array as [min, max] format
        return (lst)
    else:
        fin = []
        length = len(lst) - 1
        lst.sort()
        fin.append(lst[0])
        fin.append(lst[length])
        return (fin)
# %%
# sol 1


def min_max(lst):
    return [min(lst), max(lst)]
