# remove vowel letters in all words in sentence
# %%
# my sol


def disemvowel(string_):
    for i in string_:
        if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            string_ = string_.replace(str(i), "")
    return string_
# %%
# sol 1


def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
# %%
# sol 1


def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
# %%
# sol 2


def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i, '')
    return s
