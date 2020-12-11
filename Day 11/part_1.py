fo = open("input.txt", "r")
raw = fo.read()
strs = raw.split()

width = len(strs[0])
length = len(strs)


def neighbours(i, j, grid):
    res = []
    if i > 0:
        if j > 0:
            res.append(prev[(i-1)*width+j-1])
        res.append(prev[(i-1)*width+j])
        if j < width-1:
            res.append(prev[(i-1)*width+j+1])

    if j > 0:
        res.append(prev[i * width + j - 1])

    if j < width - 1:
        res.append(prev[i * width + j + 1])

    if i < length-1:
        if j > 0:
            res.append(prev[(i+1)*width+j-1])
        res.append(prev[(i+1)*width+j])
        if j < width-1:
            res.append(prev[(i+1)*width+j+1])

    return res.count("#")


blank = [""] * width * length
prev = list("".join(strs))
changed = True
iter = 0
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
            elif prev[i*width+j] == "#" and occupy_count >= 4:
                curr[i*width+j] = "L"
                changed = True
            else:
                curr[i*width+j] = prev[i*width+j]
    prev = curr.copy()
    # iter += 1


print(prev.count("#"))