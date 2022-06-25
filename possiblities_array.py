# %%
# my solution

def is_all_possibilities(arr):
    if (arr == []):
        return False
    else:
        arr.sort()
        arr2 = []
        for i in range(len(arr)):
            arr2.append(i)
        if (arr == arr2):
            return True
        else:
            return False
# %%
# solution 1


def is_all_possibilities(arr):
    return bool(arr) and set(arr) == set(range(len(arr)))
    # note bool checks if The object is empty, like [], (), {}
# %%
# solution 2


def is_all_possibilities(arr):
    if len(arr) == 0:
        return False
    n = len(arr) - 1
    i = 0

    for x in sorted(arr):
        if x != i:
            return False
        i += 1
    return True
