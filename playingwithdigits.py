# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k return k
# %%
# my sol
def dig_pow(n, p):
    org_no = n
    pos_nums = []
    sum = 0
    while n != 0:
        pos_nums.append(n % 10)
        n = n // 10
    digit = pos_nums[::-1]
    for i in digit:
        sum = sum + i ** p
        p += 1
    if (sum % org_no) == 0:
        return(sum/org_no)
    else:
        return(-1)

# %%
# sol 1


def dig_pow(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p+i)
    return s/n if s % n == 0 else -1
# %%
# sol 2


def dig_pow(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k
