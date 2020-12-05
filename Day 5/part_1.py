fo = open("input.txt","r")
raw = fo.read()
strs = raw.split()

strs.sort()
print(strs[0])
print((2**7+2**6+2**4+2**2)*4)
print((2**6+2**2+1)*8)
print("hi")
