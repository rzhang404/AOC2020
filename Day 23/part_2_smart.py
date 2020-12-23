fo = open("input.txt","r")
raw = fo.read()

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# circ = []
circ = {}
first = int(raw[0])
old_node = Node(first)
circ[first] = old_node
for char in raw[1:]:
    new_node = Node(int(char))
    new_node.prev = old_node
    old_node.next = new_node
    circ[int(char)] = new_node
    old_node = new_node
    # circ.append(int(char))

for i in range(999991):
    new_node = Node(i+10)
    new_node.prev = old_node
    old_node.next = new_node
    circ[i+10] = new_node
    old_node = new_node
    # circ.append(i+10)

new_node.next = circ[first]
circ[first].prev = new_node


# circ2 = [0] * 1000000
i = 0
first = circ[first]
while i < 10000000:

    # if first > 21 and (i + first - 21 + 1) < 10000000:
    #     ind = circ.index(21)
    #
    #     slice = circ[1:4]
    #
    #     circ2 = [circ[ind]] + slice + circ[(ind+1):] + [first] + circ[4:ind]
    #     circ = circ2
    #
    #     # Also rotate
    #     ind = (circ.index(first) + 1) % len(circ)
    #     circ2 = circ[ind:] + circ[:ind]
    #     circ = circ2
    #
    #
    #     i += (first-21+1)
    #
    # else:
    left, right = first.next, first.next.next.next

    destination = ((first.value-2) % 1000000) + 1  # wrap 1 to one million
    while destination == first.next.value or destination == first.next.next.value or destination == first.next.next.next.value:
        destination = ((destination-2) % 1000000) + 1

    # note that destination cannot be equal to first
    dest_node = circ[destination]
    # Detach right
    right.next.prev = first
    # Detach left
    first.next = right.next

    # Attach right
    right.next = dest_node.next
    dest_node.next.prev = right

    # Attach left
    left.prev = dest_node
    dest_node.next = left


    # rotate
    first = first.next
    i += 1

print(circ[1].next.value * circ[1].next.next.value)