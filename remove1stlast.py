# remove first and last char
# %%
# my solution


def remove_char(s):
    return(s[1:-1])
# %%
# sol 1


def remove_char(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return ''.join(s)
