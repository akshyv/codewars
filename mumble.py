# print abcd as A Bb Ccc Dddd
# %%
# sol 1
def accum(s):
    output = []
    for count, letter in enumerate(s):
        output.append(letter.upper() + letter.lower()*(count))
    return '-'.join(output)
