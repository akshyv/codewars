# write 252 as 200 + 50 + 2
# %%
# my sol
def expanded_form(num):
    result = []

    for index, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            result.append(digit + ('0' * index))

    return ' + '.join(result[::-1])
