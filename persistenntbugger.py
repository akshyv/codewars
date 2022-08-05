# try multiplying digits repeatedly such that the number is single digit eg : 24 = 4*2 = 8
# %%
# my sol
def persistence(n):
    count = 0
    t = 1
    while n > 9:
        temp = str(n)
        for j in range(len(temp)):
            t *= int(temp[j])
        count += 1
        n = t
        t = 1
    return count
