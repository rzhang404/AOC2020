fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n")


def apply_mask(mask, num, prior):
    num = bin(num)[2:]
    num = "0" * (len(mask) - len(num)) + num

    build = prior
    for i in range(len(mask)):
        if mask[i] != "X":
            build[i] = mask[i]
        else:
            build[i] = num[i]

    return build


mem = {}

blank = ["0"] * 36
mask = ""
for line in strs:
    case, equal, val = line.split()
    if case == "mask":
        mask = val
    else:
        mem[case[4:-1]] = apply_mask(mask, int(val), blank.copy())

sum = 0
for build in mem.values():
    val = 0
    for i in range(len(mask)):
        if build[-i-1] == "1":
            val += 2 ** i
    sum += val

print(sum)