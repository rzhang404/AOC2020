fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()

grid = {}

for tile in strs:
    mod = ""
    x, y = 0, 0 # collapse to ne and e axes
    for char in tile:
        if char == "n" or char == "s":
            mod = char
        else:  #
            if char == "e":
                if mod == "n":
                    x += 1
                elif mod == "":
                    y += 1
                elif mod == "s":
                    # se = e - ne
                    y += 1  # e
                    x -= 1  # -ne
            elif char == "w":
                if mod == "n":
                    # nw = ne - e
                    y -= 1  # -e
                    x += 1  # ne
                elif mod == "":
                    y -= 1
                elif mod == "s":
                    x -= 1

            mod = ""

    loc = str(x) + " " + str(y)

    truetile = grid.get(loc, +1)
    grid[loc] = truetile * -1

aux_grid = grid.copy()
for loc, truetile in aux_grid.items():
    if truetile == +1:
        grid.pop(loc, None)

# assume grid only tracks black tiles
# aux_grid = {}  # aux_grid holds next iteration of tiles
for i in range(100):
    aux_grid = grid.copy()  # save current grid
    neighbour_grid = {}   # neighbour_grid counts neighbouring black tiles
    for loc, truetile in grid.items():
        split = loc.split(" ")
        x, y = int(split[0]), int(split[1])

        neighbour_grid[str(x + 1) + " " + str(y)] = neighbour_grid.get((str(x + 1) + " " + str(y)), 0) + 1
        neighbour_grid[str(x) + " " + str(y + 1)] = neighbour_grid.get((str(x) + " " + str(y + 1)), 0) + 1
        neighbour_grid[str(x - 1) + " " + str(y + 1)] = neighbour_grid.get((str(x - 1) + " " + str(y + 1)), 0) + 1
        neighbour_grid[str(x - 1) + " " + str(y)] = neighbour_grid.get((str(x - 1) + " " + str(y)), 0) + 1
        neighbour_grid[str(x) + " " + str(y - 1)] = neighbour_grid.get((str(x) + " " + str(y - 1)), 0) + 1
        neighbour_grid[str(x + 1) + " " + str(y - 1)] = neighbour_grid.get((str(x + 1) + " " + str(y - 1)), 0) + 1



        # neighbours = 0

        # neighbours += 1 if grid.get(str(x+1) + " " + str(y), +1) == -1 else 0
        # neighbours += 1 if grid.get(str(x) + " " + str(y+1), +1) == -1 else 0
        # neighbours += 1 if grid.get(str(x-1) + " " + str(y+1), +1) == -1 else 0
        # neighbours += 1 if grid.get(str(x-1) + " " + str(y), +1) == -1 else 0
        # neighbours += 1 if grid.get(str(x) + " " + str(y-1), +1) == -1 else 0
        # neighbours += 1 if grid.get(str(x+1) + " " + str(y-1), +1) == -1 else 0
        #
        # if truetile == +1:  # White flip condition
        #     if neighbours == 2:
        #         aux_grid[loc] = -1
        #     else:
        #         aux_grid[loc] = +1
        # else:  # Black flip condition
        #     if neighbours == 0 or neighbours > 2:
        #         aux_grid[loc] = +1
        #     else:
        #         aux_grid[loc] = -1

    for loc, neighbour_count in neighbour_grid.items():
        if neighbour_count == 2:
            aux_grid[loc] = -1  # regardless of starting colour, this tile is now black, so track it

    for loc, truetile in grid.items():
        neighbour_count = neighbour_grid.get(loc, 0)
        if neighbour_count == 0 or neighbour_count > 2:
            aux_grid.pop(loc, None)  # if this tile was originally black, check if it still should be

    grid = aux_grid


total = 0
for truetile in grid.values():
    if truetile == -1:
        total += 1

print(total)

