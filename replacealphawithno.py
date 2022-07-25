# a=1 b =2 like that changwe word cat with "3 1 20"
# %%
# my sol
def alphabet_position(text):
    a2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    text = text.upper()
    no = []
    for i in text:
        if i in a2:
            index = a2.index(i) + 1
            no.append(str(index))
    return(" ".join(no))

# %%
# sol 1


def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
