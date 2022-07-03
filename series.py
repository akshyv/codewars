# take no of series for 1+(1/4)+(1/7)+(1/10)+....
# %%
# my solution


def series_sum(n):
    a = 1
    sum = 1.00
    if n == 0:
        return("%.2f" % 0.00)
    elif n == 1:
        return("%.2f" % sum)
    else:
        for i in range(1, n):
            a = a + 3
            sum = sum + (1/a)
    return("%.2f" % sum)
# %%
# solu 1


def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
# %%
# sol 2


def series_sum(n):
    sum = 0.0
    for i in range(0, n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum
