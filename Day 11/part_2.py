fo = open("input.txt", "r")
raw = fo.read()
strs = raw.split()

width = len(strs[0])
length = len(strs)


def in_bounds(i, j):
    return 0 <= i < length and 0 <= j < width


def scan(i, j, grid, direction):
    i += direction[0]
    j += direction[1]
    while in_bounds(i, j):
        if grid[i*width+j] != ".":
            return grid[i*width+j]
        i += direction[0]
        j += direction[1]

    return "W"  # Wall, discarded for all intents and purposes


def neighbours(i, j, grid):
    res = []
    cardinals = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for direction in cardinals:
        res.append(scan(i, j, grid, direction))

    return res.count("#")


blank = [""] * width * length
prev = list("".join(strs))
changed = True
# iter = 0
while changed:
    changed = False
    # print(iter)

    count = prev.count("#")
    curr = blank.copy()
    for i in range(length):
        for j in range(width):

            occupy_count = neighbours(i, j, prev)
            if prev[i*width+j] == "L" and occupy_count == 0:
                curr[i*width+j] = "#"
                changed = True
            elif prev[i*width+j] == "#" and occupy_count >= 5:
                curr[i*width+j] = "L"
                changed = True
            else:
                curr[i*width+j] = prev[i*width+j]
    prev = curr.copy()
    # iter += 1


print(prev.count("#"))