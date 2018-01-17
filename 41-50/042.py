

triangle_numbers = []
num_triangles = 0
for num in range(99):
    triangle_num = 0.5 * num * (num + 1)
    triangle_numbers.append(triangle_num)

with open('p042_words.txt') as txt_file:
    for item in txt_file:
        words = item.replace("\"", "").split(',')
        for word in words:
            test_num = 0
            for letter in word:
                test_num += (ord(letter) - 64)


            if test_num in triangle_numbers:
                num_triangles += 1

print(num_triangles)