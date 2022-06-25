# return true if string has a ending
# %%
# my solution


def solution(string, ending):
    if string.endswith(ending):
        return True
    else:
        return False


# %%
# solution 1


def solution(string, ending):
    return ending in string[-len(ending):]
# %%
# solution 2


def solution(string, ending):
    string1 = len(string) - len(ending)
    string2 = len(string) - string1
    string3 = string[string1:]
    if string3 == ending:
        return True
    else:
        return False
