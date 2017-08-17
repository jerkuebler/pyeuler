# Not really sure how to justify the way I'm reducing the values being iterated over.
# Fast result and gives all the 9-digit pandigitals for series where n > 1.


def pandigital_multiple():
    pandigital_list = []

    for list_len in range(2, 20):
        max_num = "9" * (9 // list_len + 1)
        min_num = ("1" * (10 // list_len - 1)) or 1
        print(min_num, max_num)

        for i in range(int(min_num), int(max_num)):
            factor_list = []
            for j in range(1, list_len + 1):
                factor_list.append(i * j)

            factor_str = ""
            pandigital = "123456789"
            for item in factor_list:
                factor_str += str(item)

            test_str = ''.join(sorted(factor_str))

            if test_str == pandigital:
                pandigital_list.append(int(factor_str))

    print(max(pandigital_list))


pandigital_multiple()
