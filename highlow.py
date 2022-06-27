# %%
# my solution


def high_and_low(nums):
    numbers = nums.split(' ')
    numArr = []
    for i in numbers:
        numArr.append(int(i))
        max = numArr[0]
        min = numArr[0]
    if len(numArr) != 0:
        for j in range(0, len(numArr)):
            if(numArr[j]) > max:
                max = numArr[j]
            if(numArr[j]) < min:
                min = numArr[j]
    return "%s %d" % (max, min)
# %%
# solution 1


def high_and_low(numbers):  # z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn), min(nn))
# %%
# solution 2   smart solution


def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])
