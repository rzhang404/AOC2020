fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()

product = 1
repeat = len(strs[0])  # all rows are equal width
x_rate, y_rate = [1, 3, 5, 7, 1], [1, 1, 1, 1, 2]

for i in range(5):
    x, y = 0, 0
    total = 0
    while y < len(strs):
        index = x % repeat
        if strs[y][index] == "#":
            total += 1
        x += x_rate[i]
        y += y_rate[i]
    product *= total

print(product)
