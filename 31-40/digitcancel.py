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
    cancels_list = []

    for i in range(10, 50):
        for j in range(50, 100):
            if check_num(i, j):
                cancels_list.append((i, j))

    return cancels_list


def find_product(cancels_list):

    num = 1
    den = 1
    for item in cancels_list:
        num *= item[0]
        den *= item[1]

    return num, den

cancel_list = digit_cancels()
print(cancel_list)
nums = find_product(cancel_list)
print(nums[0]/nums[1])