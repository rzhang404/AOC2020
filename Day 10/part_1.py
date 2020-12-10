
# Read input (credit gKai)
# Assumes sanitary, integer input separated by spaces
fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()
ints = [int(numeric_string) for numeric_string in strs]


ints.sort()
a, b = 0, len(ints)-1  # Point to smallest and biggest

diffs = [0] * (len(ints) -1)

for i in range(len(ints)-1):
    diffs[i] = ints[i+1] - ints[i]


#TODO: off by one answers
print(diffs.count(1) * diffs.count(3))