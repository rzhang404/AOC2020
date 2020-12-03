fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()

total = 0
for i in range(1000):
    (first, second) = strs[i*3].split("-")
    char = strs[i*3+1][0]  # take just the letter
    pw = strs[i*3+2]

    if (pw[int(first) - 1] == char) ^ (pw[int(second) - 1] == char):
        total += 1

print(total)