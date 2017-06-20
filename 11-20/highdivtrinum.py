def find_triangular_number(factors):

    divis = []
    position = 0
    num = 0

    while len(divis) < factors:
        divis = []
        position += 1
        num += position
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divis.append(i)
                divis.append(num // i)
        print(divis)
        divis = set(divis)

    return num

print(find_triangular_number(500))