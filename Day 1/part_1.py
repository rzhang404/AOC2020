
# Read input (credit gKai)
# Assumes sanitary, integer input separated by spaces
fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()
ints = [int(numeric_string) for numeric_string in strs]


ints.sort()
a, b = 0, len(ints)-1  # Point to smallest and biggest
while (a != b):
    sum = ints[a] + ints[b]
    if sum > 2020:
        # Decrease sum by
        b -= 1
    elif sum < 2020:
        # Increase sum
        a += 1
    else:  # sum == 2020
        print(ints[a]*ints[b])
        break

#TODO: prove correctness or adjust algorithm