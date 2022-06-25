# %%
def past(h, m, s):
    return h*60*60*1000+m*60*1000+1000*s
# %%
# sol 2


def past(h, m, s):
    return (s + (m + h * 60) * 60) * 1000
