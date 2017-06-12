target = 1000

def abctriplet(target):

    a = 1
    b = 1
    c = 1

    while a < target/3:
        print(a,b,c)
        a += 1
        for i in range(a):
            b = a + 1
            while b < target/2:
                c = target - a - b
                if a*a + b*b == c*c:
                    return a*b*c
                b += 1

print(abctriplet(target))