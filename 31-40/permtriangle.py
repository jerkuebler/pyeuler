# Faster to compute all of the possible values and only populate the list with parameters <= 1000


def perm_triangle(max_num):
    triangle_perms = {}

    for i in range(1, max_num):
        for j in range(1, max_num):
            k_sqr = i ** 2 + j ** 2
            k = k_sqr ** 0.5
            if k % 1 == 0:
                p = i + j + k
                if p <= max_num:
                    if p in triangle_perms:
                        triangle_perms[int(p)] += 1
                    else:
                        triangle_perms[int(p)] = 1

    return max(triangle_perms, key=(lambda key: triangle_perms[key]))


print(perm_triangle(1000))
