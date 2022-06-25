# %%
# my solution

def avg(number):
    return sum(number)/len(number)
# %%
# better solution


def avg(number):
    return sum(number)/len(number) if len(number) != 0 else 0
