# if n = 5 print [5,4,3,2,1]
# %%
# my solution


def reverse_seq(n):
    array = [n]
    for i in range(1, n):
        array.append(n-1)
        n -= 1
    return array
# %%
# solution 1


def reverseseq(n):
    return list(range(n, 0, -1))
# %%
# sol 2
