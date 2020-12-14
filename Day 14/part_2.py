fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n")


def construct_value(build):
    val = 0
    for i in range(len(mask)):
        if build[-i - 1] == "1":
            val += 2 ** i
    return val


def apply_mask(mask, num, prior):
    # for i in range(len(mask)):
    #     if mask[i] == "X":
    #         list1 = build.copy().append("0")
    #         list2 = build.copy().append("1")
    #         # Concat the both
    #         return apply_mask(mask, num, list1, i + 1) + apply_mask(mask, num, list2, i + 1)
    #     elif mask[i] == "1":
    #         build.append("1")
    #         return apply_mask(mask, num, build, i+1)
    #     else:
    #         build.append(num[i])
    #         return apply_mask(mask, num, build, i+1)
    worklist = [(prior, 0)]
    retlist = []
    while len(worklist) > 0:
        next_build, i = worklist.pop(0)
        if i >= 36:
            retlist.append(construct_value(next_build))
            continue

        if mask[i] == "1":
            next_build.append("1")
            worklist.append((next_build, i+1))
        elif mask[i] == "0":
            next_build.append(num[i])
            worklist.append((next_build, i+1))
        else:
            list2 = next_build.copy()
            next_build.append("0")
            list2.append("1")
            worklist.append((next_build, i+1))
            worklist.append((list2, i+1))

    return retlist


mem = {}

blank = ["0"] * 36
mask = ""
for line in strs:
    case, equal, val = line.split()
    if case == "mask":
        mask = val
    else:
        addr = int(case[4:-1])

        num = bin(addr)[2:]
        num = "0" * (len(mask) - len(num)) + num
        list = apply_mask(mask, num, [])
        for addr in list:
            mem[addr] = int(val)

sum = 0
for value in mem.values():
   sum += value




print(sum)