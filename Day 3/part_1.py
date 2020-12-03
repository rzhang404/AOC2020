fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()

x = 0
total = 0
repeat = len(strs[0])  # all rows are equal width
for row in strs:
    index = x % repeat
    if row[index] == "#":
        total += 1
    x += 3

print(total)
