fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n\n")


total = 0
for group in strs:

    set1 = set()
    set2 = set()

    persons = group.split()

    # Initialize the set of possibilities to the first person's answers
    for char in persons[0]:
        set1.add(char)

    # For each other person
    for person in persons[1:]:
        set2 = set1.copy()
        for char in person:
            set2.discard(char)
        for char in set2:
            set1.discard(char)

    # set.discard("\n")
    total += len(set1)

print(total)