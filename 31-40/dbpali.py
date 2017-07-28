def double_base_palindrome(num):
    if str(num) == str(num)[::-1]:
        bin_num = bin(num)[2:]
        if bin_num == bin_num[::-1]:
            return True
    return False


def check_range(max_num):
    db_list = []

    for num in range(max_num):
        if double_base_palindrome(num):
            db_list.append(num)

    return db_list


dbp_list = check_range(1000000)
print(dbp_list)
print(sum(dbp_list))
