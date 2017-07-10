def fiblen(num_len):

    temp = 0
    temp2 = 1
    new_num = 0
    index = 0

    while len(str(new_num)) < num_len:
        new_num = temp + temp2
        temp2, temp = temp, new_num
        index += 1

    return index

print(fiblen(1000))