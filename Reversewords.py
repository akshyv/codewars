# print this is example! as siht si !elpmaxe
# %%
# my sol
def reverse_words(str):
    strList = []
    for word in str.split(' '):
        strList.append(word[::-1])
    return ' '.join(strList)
# %%
# sol 1


def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
