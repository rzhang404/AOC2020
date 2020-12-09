
# Read input (credit gKai)
# Assumes sanitary, integer input separated by spaces
fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()
ints = [int(numeric_string) for numeric_string in strs]


invalid = 0
for i in range(975):
    found = False
    index = i + 25
    for j in range(25):
        for k in range(25-j):  # would be incorrect if one number is exactly half of another
            if ints[index] == (ints[index-j-1] + ints[index-j-k-1]):
                found = True

    if not found:
        invalid = ints[index]


for i in range(1000):
    sum = 0
    smallest = 99999999999999999999
    largest = 0
    j=i
    while j < 1000 and sum < invalid:
        sum += ints[j]
        smallest = min(smallest, ints[j])
        largest = max(largest, ints[j])
        if sum == invalid:
            print(smallest + largest)
            break
        j += 1
