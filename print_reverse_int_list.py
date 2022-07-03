# print 123 as [3,2,1]
# %%
# my solution


def digitize(n):
    list = []
    a = str(n)[::-1]
    for i in (a):
        list.append(int(i))
    return list
# %%
# sol 1


def digitize(n):
    return map(int, str(n)[::-1])
