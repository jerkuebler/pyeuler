def power_digit_sum(number):

    digits = 2 ** number
    nums = str(digits)
    sum = 0

    for i in nums:
        sum += int(i)

    return sum


print(power_digit_sum(1000))