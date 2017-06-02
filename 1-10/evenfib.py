def fib(n):

    temp = 0
    temp2 = 1
    resultn = 0
    while 1:
        new_num = temp + temp2
        if new_num > n:
            break
        temp2, temp = temp, new_num
        if new_num % 2 == 0:
            resultn += new_num

    return resultn

print(fib(4000000))