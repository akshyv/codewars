# tribonacci series [0,0,1] n = 6 gives [0,0,1,1,2,4]
# %%
# my sol


def tribonacci(signature, n):
    if n == 0:
        return([])
    elif n != 0 and n <= 3:
        sign = []
        for i in range(n):
            sign.append(signature[i])
        return(sign)
    else:
        for i in range(3, n):
            signature.append(signature[i-1]+signature[i-2]+signature[i-3])
        return(signature)
# %%
# sol 1


def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res
# %%
# sol 2


def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]
