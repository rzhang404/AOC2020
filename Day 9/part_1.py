
# Read input (credit gKai)
# Assumes sanitary, integer input separated by spaces
fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()
ints = [int(numeric_string) for numeric_string in strs]



for i in range(975):
    found = False
    index = i + 25
    for j in range(25):
        for k in range(25-j):
            if ints[index] == (ints[index-j-1] + ints[index-j-k-1]):
                found = True

    if not found:
        print(ints[index])