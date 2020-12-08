fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n")


def read_arg(arg):
    if arg[0] == "+":
        return int(arg[1:])
    else:
        return -int(arg[1:])


for j in range(len(strs)):
    ins_plus_arg = strs[j].split()
    ins = ins_plus_arg[0]

    if ins == "acc":
        continue

    if ins == "nop":
        replace = "jmp " + ins_plus_arg[1]
    if ins == "jmp":
        replace = "nop " + ins_plus_arg[1]

    loop_copy = strs.copy()
    loop_copy[j] = replace

    total = 0
    i = 0
    times_run = [0] * len(strs)
    while times_run[i] == 0:

        times_run[i] += 1

        ins_plus_arg = loop_copy[i].split()
        ins = ins_plus_arg[0]
        if ins == "acc":
            total += read_arg(ins_plus_arg[1])
            i += 1
        elif ins == "jmp":
            i += read_arg(ins_plus_arg[1])
        elif ins == "nop":
            print("nop!")
            i += 1

        if i == len(strs):
            print(total)
            # break

print(total)