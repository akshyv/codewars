# if b has elements of a remove those in a
# %%
# sol 1

def array_diff(a, b):
    c = []
    if len(b) == 0:
        return (a)
    for i in a:
        if i not in b:
            c.append(i)
    return (c)
# %%
# sol 1


def array_diff(a, b):
    return [x for x in a if x not in b]
