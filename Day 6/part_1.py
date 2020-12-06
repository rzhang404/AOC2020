fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n\n")


total = 0
for group in strs:
    set = {"a"}
    set.discard("a")  # Python does not allow empty set initialization
    for char in group:
        set.add(char)

    set.discard("\n")
    total += len(set)

print(total)
