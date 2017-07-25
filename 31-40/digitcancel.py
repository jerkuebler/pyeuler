def check_num(numerator, denominator):
    special_number = '0'
    for i in str(numerator):
        if i in str(denominator):
            special_number = i

    if special_number != '0':
        new_num_str = str(numerator).replace(special_number, '')
        new_den_str = str(denominator).replace(special_number, '')
        if new_num_str != '' and new_den_str != '':
            new_num = int(new_num_str)
            new_den = int(new_den_str)
            if new_den != 0 and new_num != new_den:
                if new_num / new_den == numerator / denominator:
                    return True

    return False


def digit_cancels():
    nums = []

    for i in range(10, 50):
        for j in range(10, 100):
            if check_num(i, j):
                nums.append((i, j))

    return nums


def find_product(list_cancels):

    num = 1
    den = 1
    for item in list_cancels:
        num *= item[0]
        den *= item[1]

    return num, den

nums = find_product(digit_cancels())
print(nums[0]/nums[1])