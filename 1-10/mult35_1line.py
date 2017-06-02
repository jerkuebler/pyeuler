def mult35(below):

    return sum(num for num in range(below) if (num % 5 == 0) or (num % 3 == 0))

print(mult35(1000))
