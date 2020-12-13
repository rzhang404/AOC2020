fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()

time = int(strs[0])
buses = strs[1].split(',')


mindep = time*2
for bus in buses:
    if bus != "x":
        bint = int(bus)
        btime = bint * (time // bint +1)

        if btime < mindep:
            mindep = btime
            bid = bint

print((mindep-time)*bid)