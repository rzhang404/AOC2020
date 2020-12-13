fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()

time = int(strs[0])  # ignored
buses = strs[1].split(',')

mindep = 0
rotation = 1
cares = []
# for offset, bus in enumerate(buses):
#     if bus != "x":
#         bint = int(bus)
#         while mindep % bint != (offset % bint):
#             mindep += rotation
#         print("bus" + bus + "considered, with rotation", rotation, "mindep", mindep, "offset", mindep%bint, offset%bint)
#         rotation *= bint

for offset, bus in enumerate(buses):
    if bus != "x":
        bint = int(bus)
        while (mindep +offset) % bint != 0:
            mindep += rotation
        print("bus" + bus + "considered, with rotation", rotation, "mindep", mindep, "offset", mindep%bint, offset%bint)
        rotation *= bint



print(mindep)