# find sum of least two numbers in an array
# %%
# My sol


from heapq import nsmallest


def sum_two_smallest_numbers(numbers):
    numbers.sort()
    result = numbers[0] + numbers[1]
    return result
# %%
# sol 1


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
# %%
# sol 2


def sum_two_smallest_numbers(numbers):
    smallest1 = None
    smallest2 = None
    for n in numbers:
        if not smallest1 or n < smallest1:
            smallest2 = smallest1
            smallest1 = n
        elif not smallest2 or n < smallest2:
            smallest2 = n
    return smallest1 + smallest2

# %%
# sol 3


def sum_two_smallest_numbers(numbers):
    return sum(nsmallest(2, numbers))
