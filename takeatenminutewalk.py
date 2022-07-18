# check if there are 10 direction if yes then check the person's start point and end point is same
# %%
# my sol
def is_valid_walk(walk):
    if(len(walk) != 10):
        return False
    else:
        N = 0
        S = 0
        W = 0
        E = 0
        for i in walk:
            if (i == 'w'):
                W += 1
            elif (i == 'e'):
                E += 1
            elif (i == 's'):
                S += 1
            else:
                N += 1
        return((N == S) and (W == E))

# %%
# sol 1 same sol as mine but better code


def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

# %%
# sol 2


def isValidWalk(walk):
    if len(walk) != 10:
        return False

    x, y = 0, 0

    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
        else:
            return False

    return x == 0 and y == 0
