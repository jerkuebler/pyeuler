def largepalin(digits):
    
    movement = 0
    result = None

    def mainloop(m):
        start = int('9' * digits)
        end = int('9' * (digits - m) + '0' * m)
        for i in range(start, end, -1):
            for j in range(start, end, -1):
                num = i * j
                check = str(num)
                lenn = len(check) // 2
                if check[:lenn] == check[-lenn:][::-1]:
                    print("i = ", i, " ", "j = ", j)
                    return num

    while result is None:
        movement += 1
        result = mainloop(movement)

    return result

print(largepalin(7))
