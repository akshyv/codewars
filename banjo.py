# %%
# my solution

def areYouPlayingBanjo(name):
    if (name[0] == 'r') or (name[0] == 'R'):
        # note : there is a method to do this
        # if name.startswith('R') or name.startswith('r'): instead of name[0]
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
# %%
# solution 1


def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"

# %%
# solution 2


def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
