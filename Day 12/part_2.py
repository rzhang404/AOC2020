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
        angle += length
        if angle >= 360:
            angle -= 360
    elif code == "R":
        angle -= length
        if angle < 0:
            angle += 360
    elif code == "F":
        if angle == 90:
            y += length * way_x
            x -= length * way_y
        elif angle == 270:
            y -= length * way_x
            x += length * way_y
        elif angle == 180:
            x -= length * way_x
            y -= length * way_y
        elif angle == 0:
            x += length * way_x
            y += length * way_y

print(abs(x)+abs(y))