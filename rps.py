# rock paper scissors
# %%
# my sol
def rps(p1, p2):
    if (p1 == p2):
        return "Draw!"
    else:
        rules = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
    if (rules[p1] == p2):
        return ('Player 1 won!')
    else:
        return ('Player 2 won!')
# %%
# sol 1


def rps(p1, p2):
    hand = {'rock': 0, 'paper': 1, 'scissors': 2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]
