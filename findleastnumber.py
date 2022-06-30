# find the smallest number
# %%
# my solution

def find_smallest_int(arr):
    arr.sort()
    return arr[0]

# %%
# my solution 2


def find_smallest_int(arr):
    small = arr[0]
    for i in arr:
        if i < small:
            small = i
    return small
# %%
# soltion 1


def findSmallestInt(arr):
    return min(arr)
