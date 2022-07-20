# convert "camelCasing"  =>  "camel Casing"
# %%
# my sol
import re


def solution(s):
    return "".join([" " + c if c.isupper() else c for c in s])

# %%
# sol 1


def solution(s):
    return re.sub('([A-Z])', r' \1', s)
