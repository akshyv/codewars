# print [1,2,3] as [2,4,6]
# %%
# my sol
def maps(a):
    b = []
    for i in a:
        i = i * 2
        b.append(i)
    return b
# %%
# sol 1


def maps(a):
    return [2 * x for x in a]
