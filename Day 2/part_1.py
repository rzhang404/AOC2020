fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()

total = 0
for i in range(1000):
    (lower, upper) = strs[i*3].split("-")
    char = strs[i*3+1][0]  # take just the letter
    pw = strs[i*3+2]

    count = pw.count(char)
    if (count >= int(lower) and count <= int(upper)):
        total += 1

print(total)