fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()

import math

x = 0
y = 0
way_x = 10
way_y = 1
angle = 0
for ins in strs:
    code = ins[0]
    length = int(ins[1:])



    if code == "N":
        way_y += length
    elif code == "S":
        way_y -= length
    elif code == "W":
        way_x -= length
    elif code == "E":
        way_x += length
    elif code == "L":
        if length == 90:
            way_x, way_y = -way_y, way_x
        elif length == 180:
            way_x, way_y = -way_x, -way_y
        elif length == 270:
            way_x, way_y = way_y, -way_x
    elif code == "R":
        if length == 90:
            way_x, way_y = way_y, -way_x
        elif length == 180:
            way_x, way_y = -way_x, -way_y
        elif length == 270:
            way_x, way_y = -way_y, way_x
    elif code == "F":
        x += length * way_x
        y += length * way_y

print(abs(x)+abs(y))