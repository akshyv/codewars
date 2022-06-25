# %%
# my solution

def count_positives_sum_negatives(arr):
    positive_count = 0
    negative_sum = 0
    for n in arr:
        if n > 0:
            positive_count += 1
        elif n < 0:
            negative_sum += n
    if (len(arr) == 0):
        return ([])
    else:
        return([positive_count, negative_sum])
# %%
# solution 1


def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []
# %%
# solution 2


def count_positives_sum_negatives(arr):
    return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []
