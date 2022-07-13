# represent sum of  two numbers in binary format
# %%
# my sol
def add_binary(a, b):
    c = a + b
    return bin(c).replace('0b', '')
# %%
# sol 1


def add_binary(a, b):
    print(format(a + b, 'b'))


add_binary(2, 3)
