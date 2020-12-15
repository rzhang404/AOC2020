fo = open("input.txt","r")
raw = fo.read()
strs = raw.split(",")


age = {}

i = 0
for val in strs:
    num = int(val)
    age[num] = i
    prevnum = num
    i += 1

while i < 30000000:
    if i % 300000 == 0:
        print(i)

    tmp = age.get(num, -1)
    age[num] = i-1
    if tmp == -1:
        num = 0
    else:
        num = i-tmp-1
    i += 1

print(num)