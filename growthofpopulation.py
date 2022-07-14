# how much time it takes for population to reach a given target value if given percentage raises per year and given amount raise per year
# %%
# my sol

def nb_year(p0, percent, aug, p):
    t = 0
    while p0 < p:
        # my mathematical brain hates that I need to round this
        p0 = int(p0*(1 + percent/100)) + aug
        t += 1
    return t

# %%
# sol 1


def nb_year(p0, percent, aug, p, years=0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years
