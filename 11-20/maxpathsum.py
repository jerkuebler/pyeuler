# start at the bottom right. Chose which of the two is better for the number above it. Do this for each number in the
# top set.


def find_path(trifile):

    triangle = []

    with open(trifile, 'r') as trinums:
        for item in trinums:
            nums = item.split()
            triangle.append(nums)

    for i in range(len(triangle) - 2, -1, -1):
        for j, k in enumerate(triangle[i]):
            triangle[i][j] = max(int(triangle[i][j]) + int(triangle[i+1][j]), int(triangle[i][j]) + int(triangle[i+1][j+1]))

    return triangle


print(find_path('triangle.txt'))