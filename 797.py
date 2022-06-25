# %%
# my solution

import re


def seven_ate9(str_):
    if len(str_) < 3:
        return str_
    i = 1
    s = list(str_)
    while i < len(s) - 1:
        if s[i] == '9' and s[i - 1] == '7' and s[i + 1] == '7':
            del s[i]
            continue
        i += 1
    return ''.join(s)

# %%
# solution 1


def seven_ate9(str_):
    while str_.find('797') != -1:
        str_ = str_.replace('797', '77')
    return

# %%
# solution 2


def seven_ate9(str_):
    return re.sub(r'79(?=7)', r'7', str_)
