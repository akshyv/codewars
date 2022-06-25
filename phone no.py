# write phone no in (xyz) abc defg format
# %%
# solution 1


def create_phone_number(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"

# %%
# solution 2


def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    # format is the python's version for using `${varname}` in js
    # another format is print/return ("%s"%varname)
