fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()

import math

x = 0
y = 0
angle = 0
for ins in strs:
    code = ins[0]
    length = int(ins[1:])



    if code == "N":
        y += length
    elif code == "S":
        y -= length
    elif code == "W":
        x -= length
    elif code == "E":
        x += length
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
            y += length
        elif angle == 270:
            y -= length
        elif angle == 180:
            x -= length
        elif angle == 0:
            x += length

print(abs(x)+abs(y))