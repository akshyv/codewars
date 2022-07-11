# replace unrepeat letters with '(' and repeated letter with ')'
# %%
# my failed solution
def duplicate_encode(word):
    letter = []
    repeat = []
    newword = ''
    for i in word:
        if i not in letter:
            letter. append(i)
        else:
            repeat.append(i)
        if str(i) in repeat:
            print(i)
            i = ')'
        else:
            print(';;;;', i)
            i = '('
        newword = newword + i
    print(newword)

# %%
# my sol


def duplicate_encode(word):
    return "".join(["(" if word.lower().count(x) == 1 else ")" for x in word.lower()])
# %%
# sol 1


def duplicate_encode(word):
    word = word.lower()
    result = ""
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("

    return result
