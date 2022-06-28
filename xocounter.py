# if no of x = no of o
# %%
# my solution


from collections import Counter


def xo(s):
    xcount = 0
    ocount = 0
    s1 = s.lower()
    for i in s1:
        if i == "x":
            xcount += 1
        elif i == "o":
            ocount += 1
    if xcount == ocount:
        return True
    else:
        return False
# %%
# solution 1


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
# %%
# solution 2


def xo(s):
    d = Counter(s.lower())
    return d.get('x', 0) == d.get('o', 0)
