# remove duplcate characters from two strings , and print bigger string in order
# %%
# my sol
# import is not used here but used in sol 2
import itertools


def longest(s1, s2):
    return "".join(sorted([c for c in set(s1 + s2)]))
# %%
# sol 1


def longest(s1, s2):
    x = ''
    y = sorted(s1+s2)

    for i in y:
        if i not in x:
            x += i

    return x  # your code
# %%
# sol 2 used itertools here


def longest(s1, s2):
    longest = ""
    for i in s1:
        if i not in longest:
            longest += i
    for i in s2:
        if i not in longest:
            longest += i
    return ''.join(sorted(longest))
