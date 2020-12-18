fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n")

from collections import deque


# Smoother implementation with regex to grah interior brackets

total = 0
for eq in strs:
    stall = [-1]* 20
    reserves = [-1]* 20
    instr = [""] * 20
    level = 0
    curr_num = None
    op = None
    reserve = None

    for char in eq:
        if char == " ":
            continue

        if char.isnumeric():
            if curr_num is None:
                curr_num = int(char)
            elif op is not None:
                if op == "+":
                    curr_num = curr_num + int(char)
                elif op == "*":
                    reserve = curr_num
                    curr_num = int(char)
                op = None
        elif char == "+":
            op = "+"
        elif char == "*":
            op = "*"
            if reserve is not None:  # something waiting to multiply
                curr_num = reserve * curr_num
                reserve = None
        elif char == "(":
            stall[level] = curr_num
            curr_num = None
            instr[level] = op
            op = None
            reserves[level] = reserve
            reserve = None
            level += 1
        elif char == ")":
            if reserve is not None:
                curr_num = reserve * curr_num
            level -= 1
            op = instr[level]
            reserve = reserves[level]
            reserves[level] = -1
            instr[level] = ""
            right = curr_num
            curr_num = stall[level]
            stall[level] = -1

            if curr_num is None:
                curr_num = right
            elif op is not None:
                if op == "+":
                    curr_num = curr_num + right
                elif op == "*":
                    reserve = curr_num
                    curr_num = right
                op = None

    if reserve is not None:
        curr_num = reserve * curr_num

    total += curr_num

print(total)