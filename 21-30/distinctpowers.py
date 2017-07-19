def distinct_powers(max_num):

    term_list = []

    for a in range(2, max_num + 1):
        for b in range(2, max_num + 1):
            term_list.append(a ** b)

    return len(set(term_list))

print(distinct_powers(100))