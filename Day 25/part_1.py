fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()


first_key = int(strs[0])
loop_size = 0
sub_no = 7
val = 1
while val != first_key:
    loop_size += 1
    val = (val * sub_no) % 20201227


sub_no = int(strs[1])
val = 1
for i in range(loop_size):
    val = (val * sub_no) % 20201227


print(val)