# check if a sentence has all alphabet
# %%
# my sol
import string


def is_pangram(s):
    set = []
    s = s.lower()
    for i in s:
        if i.isalpha():
            if i not in set:
                set.append(i)
    return len(set) == 26

# %%
# sol 1


def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())

# %%
# sol 2


def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
