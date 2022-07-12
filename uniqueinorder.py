# get string like AABcdEAAabc and return only once therepeated letter in a cycle but repeat 7 th A because new cycle starts
# %%
# my solution (dint solve first attempt test case ['A'])


def unique_in_order(iterable):
    new_list = []
    if len(iterable) == 1:
        new_list.append(iterable)
    for i in range(len(iterable)):
        if iterable[i-1] != iterable[i]:
            new_list.append(iterable[i])
    return(new_list)
# %%
# my sol 2


def unique_in_order(iterable):
    newList = []
    for item in iterable:
        if len(newList) < 1 or not item == newList[len(newList) - 1]:
            newList.append(item)
    return newList
# %%
# sol 1


def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
# %%
# sol 2


def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res
