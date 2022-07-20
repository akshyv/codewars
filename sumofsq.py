# given array print sum of all sq of no in array
# %%
# my sol
def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum = sum + (i*i)
    return sum
# %%
# sol 1


def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
