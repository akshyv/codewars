# %%
# my solution


def is_uppercase(inp):
    return (True if inp == inp.upper() else False)


# %%
# solution 1


def is_uppercase(inp):
    return inp.upper() == inp
# %%
# Solution 2


class Word:

    def __init__(self, string=None):
        self.string = string

    def isup(self, string):
        if ord(string)-96 > 0:
            if not string.isalpha():
                return True
            return False
        return True

    def is_upper(self):
        string = self.string
        for i in range(len(string)):
            if not (self.isup(string[i])):
                return False
        return True


def is_uppercase(string):
    a = Word(string)
    return a.is_upper()
# %%
# solution 3


def is_uppercase(inp):
    from re import search
    if search(r'[a-z]', inp):
        return False
    return True
