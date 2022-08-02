# queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

#queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

#queue_time([2,3,10], 2)
# should return 12
# %%
# sol 1
def queue_time(customers, n):
    tills = [0]*n
    for i in customers:
        tills[0] += i
        tills.sort()
    return max(tills)
