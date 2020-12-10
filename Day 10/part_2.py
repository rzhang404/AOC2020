
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


def combinations(run):
    if run == 4:
        return 2 ** (run - 1) -1

    return 2 ** (run - 1)  # Choose every adaptor or not, individually




j = 0
product = 1
bigrun=0
while j < len(diffs):
    if diffs[j] == 3:
        j += 1
        continue

    run = 0
    while j < len(diffs) and diffs[j] == 1:  # breaks out if diff is 3 and is unskippable
        run += 1
        j += 1

    bigrun = max(run, bigrun)
    product *= combinations(run)


print(product * 2)  # accounting for leading optional