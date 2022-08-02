# check if smileys eyes and mouth are imp but nose is opt eyes char are ; and : nose char are - and ~ moth char are ) and D
# %%
# my sol
from re import findall


def count_smileys(arr):
    count = 0
    for s in arr:
        if len(s) == 2 and s[0] in [":", ";"] and s[-1] in [")", "D"]:
            count += 1
        elif len(s) > 2 and s[0] in [":", ";"] and s[1] in ["-", "~"] and s[-1] in [")", "D"]:
            count += 1
    return count

# %%
# Sol 1 using regex


def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
# %%
# sol 2


def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count
