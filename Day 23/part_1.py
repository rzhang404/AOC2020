fo = open("input.txt","r")
raw = fo.read()

from collections import deque


circ = deque()
for char in raw:
    circ.append(int(char))


for i in range(100):
    # peek left
    first = circ.popleft()

    second = circ.popleft()
    third = circ.popleft()
    fourth = circ.popleft()

    circ.appendleft(first)

    destination = ((first-2) % 9) + 1  # wrap 1 to 9
    while circ.count(destination) == 0:
        destination = ((destination-2) % 9) + 1

    curr = circ.popleft()
    while curr != destination:
        circ.append(curr)
        curr = circ.popleft()

    circ.appendleft(fourth)
    circ.appendleft(third)
    circ.appendleft(second)

    # back to current
    while curr != first:
        circ.append(curr)
        curr = circ.popleft()

    # let new first cup next round be the following one
    circ.append(curr)

print("hi")