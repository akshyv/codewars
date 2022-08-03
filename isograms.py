# check if word has repeated letters
# %%
# my sol
def is_isogram(string):
    word = string.lower()
    return True if word and len(set(word)) == len(word) or len(word) == 0 else False
# %%
# sol 1


def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True
