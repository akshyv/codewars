# form a sentence using words in an array
# %%
# my sol

def smash(words):
    s = ' '
    s = s.join(words)
    return(s)
# %%
# sol 1


def smash(words):
    return " ".join(words)

# %%
# sol 2


def smash(x): return " ".join(x)
# no need to return but to print output try print(smash(<some array>))
