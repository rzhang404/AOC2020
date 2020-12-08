fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n")

times_run = [0] * len(strs)

def read_arg(arg):
    if arg[0] == "+":
        return int(arg[1:])
    else:
        return -int(arg[1:])


total = 0
i = 0
while True:
    if times_run[i] > 0:
        break
    times_run[i] += 1

    split = strs[i].split()
    ins = split[0]
    if ins == "acc":
        total += read_arg(split[1])
        i += 1
    elif ins == "jmp":
        i += read_arg(split[1])
    else:
        i += 1
        continue

print(total)