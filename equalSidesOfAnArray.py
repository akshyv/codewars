# if arr = [1,2,3,4,3,2,1] print index of 4 becasue sum of b4 after the index are same
# %%
# my sol
def find_even_index(arr):

    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i

    return -1
