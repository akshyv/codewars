# for n print sum of 0+1+.....+n
# %%
# my solution
def summation(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return(sum)
# %%
# sol 1


def summation(num):
    return sum(range(num + 1))
# %%
# sol 2


def summation(num):
    return (1+num) * num / 2
