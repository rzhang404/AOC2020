fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()

grid = {}

for tile in strs:
    mod = ""
    loc = [0, 0]  # collapse to ne and e axes
    for char in tile:
        if char == "n" or char == "s":
            mod = char
        else:  #
            if char == "e":
                if mod == "n":
                    loc[0] += 1
                elif mod == "":
                    loc[1] += 1
                elif mod == "s":
                    # se = e - ne
                    loc[1] += 1  # e
                    loc[0] -= 1  # -ne
            elif char == "w":
                if mod == "n":
                    # nw = ne - e
                    loc[1] -= 1  # -e
                    loc[0] += 1  # ne
                elif mod == "":
                    loc[1] -= 1
                elif mod == "s":
                    loc[0] -= 1

            mod = ""

    truetile = grid.get(str(loc), +1)
    grid[str(loc)] = truetile * -1


total = 0
for truetile in grid.values():
    if truetile == -1:
        total += 1

print(total)

