total = 0

for num in range(1000):
    num += 1
    total += num ** num

print(str(total)[-10:])