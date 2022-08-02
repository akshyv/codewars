# if a number in list is unque return it
# %%
# my sol
def find_uniq(arr):
    for i in range(len(arr)):
        if arr[i] != arr[i+1] and arr[i+1] != arr[i+2]:
            return arr[i+1]
        elif arr[0] != arr[-1] and arr[0] != arr[1]:
            return arr[0]
        elif arr[0] != arr[-1] and arr[-2] != arr[-1]:
            return arr[-1]
# %%
# sol 1


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
