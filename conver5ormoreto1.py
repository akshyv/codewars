# if number < 5 convert to zero else convert to 1
# %%
# my solution

def fake_bin(s):
    return ''.join('0' if int(c) < 5 else '1' for c in s)
# %%
# solution 1


def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result
