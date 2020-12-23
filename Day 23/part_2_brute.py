fo = open("input.txt","r")
raw = fo.read()

circ = []
for char in raw:
    circ.append(int(char))

for i in range(999991):
    circ.append(i+10)


for i in range(10000000):
    # peek left
    first = circ[0]

    slice = circ[1:4]

    destination = ((first - 2) % 1000000) + 1  # wrap 1 to one million
    while slice.count(destination) > 0:
        destination = ((destination - 2) % 1000000) + 1

    # note that destination cannot be equal to first
    ind = circ.index(destination)
    circ2 = [circ[ind]] + slice + circ[(ind + 1):] + [first] + circ[4:ind]
    circ = circ2

    # Also rotate
    ind = (circ.index(first) + 1) % len(circ)
    circ2 = circ[ind:] + circ[:ind]
    circ = circ2


ind = circ.index(1)
print(circ[ind+1] * circ[ind+2])