def prepgrid(gridfile):
    finalgrid = []

    with open(gridfile, 'r') as grid:
        for item in grid:
            nums = item.split()
            finalgrid.append(nums)

    return finalgrid


def largestgridproduct(gridfile):
    grid = prepgrid(gridfile)
    height = len(grid)
    length = len(grid[0])
    largest = 0

    for i in range(height):
        for j in range(length):
            largest = max(
                directionalproduct(grid, (i, j), (1, 0), 4),  # horizontal
                directionalproduct(grid, (i, j), (0, 1), 4),  # vertical
                directionalproduct(grid, (i, j), (1, 1), 4),  # right diagonal
                directionalproduct(grid, (i, j), (1, -1), 4),  # left diagonal
                largest
            )


    return largest

def directionalproduct(grid, start, direction, steps):

    x0, y0 = start
    dx, dy = direction

    if not(0 <= y0 < len(grid) and
           0 <= y0 + (steps - 1)*dy < len(grid) and
           0 <= x0 < len(grid[y0]) and
           0 <= x0 + (steps - 1)*dx < len(grid[y0])):
        return 0

    product = 1
    for n in range(steps):
        product *= int(grid[y0 + n*dy][x0 + n*dx])
    return product

print(largestgridproduct('grid.txt'))
