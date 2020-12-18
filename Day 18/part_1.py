fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n")

from collections import deque


# Smoother implementation with regex to grah interior brackets

total = 0
for eq in strs:
    stall = [-1]* 20
    instr = [""] * 20
    level = 0
    left_num = None
    op = None

    for char in eq:
        if char == " ":
            continue
        elif char.isnumeric():
            if left_num is None:
                left_num = int(char)
            elif op is not None:
                if op == "+":
                    left_num = left_num + int(char)
                elif op == "*":
                    left_num = left_num * int(char)
                op = None
        elif char == "+":
            op = "+"
        elif char == "*":
            op = "*"
        elif char == "(":
            stall[level] = left_num
            left_num = None
            instr[level] = op
            op = None
            level += 1
        elif char == ")":
            level -= 1
            op = instr[level]
            instr[level] = ""
            right = left_num
            left_num = stall[level]
            stall[level] = -1

            if left_num is None:
                left_num = right
            elif op is not None:
                if op == "+":
                    left_num = left_num + right
                elif op == "*":
                    left_num = left_num * right
                op = None

    total += left_num

print(total)