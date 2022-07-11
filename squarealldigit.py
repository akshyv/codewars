# take int like 9118 and return int 811164 square all digit
# %%
# my solution


def square_digits(num):
    number = str(num)
    ans = ''
    for i in number:
        digit = int(i)
        square = str(digit*digit)
        ans = ans + square
    return(int(ans))
# %%
# sol 1


def square_digits(num):
    r = ''
    for l in str(num):
        r = r + str((int(l))**2)
    return int(r)
# %%
# sol 2


def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
