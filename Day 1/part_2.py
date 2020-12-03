
# Read input (credit gKai)
# Assumes sanitary, integer input separated by spaces
fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()
ints = [int(numeric_string) for numeric_string in strs]


ints.sort()
c = len(ints)-1  # Point to biggest
while c != 0:
    a, b = 0, c-1  # Point to smallest and biggest less than c
    remainder = 2020-ints[c]
    while a != b:
        sum = ints[a] + ints[b]
        if sum > remainder:
            # Decrease sum by
            b -= 1
        elif sum < remainder:
            # Increase sum
            a += 1
        else:  # sum == 2020
            print(ints[a]*ints[b]*ints[c])
            break
    c -= 1
