def small_mult(nums):

    factors = [i for i in range(1, nums)]
    result = None
    j = nums

    while result is None:
        j += nums
        if all(j % k == 0 for k in factors):
                result = j

    return result

print(small_mult(20))