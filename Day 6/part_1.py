fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n\n")


total = 0
for group in strs:
    questions_answered = set()

    # Any answer from anyone is valid
    for char in group:
        questions_answered.add(char)

    # Except for newline
    questions_answered.discard("\n")
    total += len(questions_answered)

print(total)
