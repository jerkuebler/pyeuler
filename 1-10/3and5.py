def mult35(below):

    i = 0
    for num in range(below):
        if (num % 5 == 0) or (num % 3 == 0):
            i += num
    return i

print(mult35(1000))
