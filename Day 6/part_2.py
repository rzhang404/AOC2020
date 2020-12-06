fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n\n")


total = 0
for group in strs:

    # Python does not allow empty set initialization
    set1 = {"a"}
    set2 = {"a"}
    set1.discard("a")
    set2.discard("a")

    persons = group.split()
    for char in persons[0]:
        set1.add(char)
    for person in persons[1:]:
        set2 = set1.copy()
        for char in person:
            set2.discard(char)
        for char in set2:
            set1.discard(char)

    # set.discard("\n")
    total += len(set1)

print(total)