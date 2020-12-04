fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n\n")

total = 0
standard_set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",}
for passport in strs:
    entries = passport.split()
    fields = set()
    for entry in entries:
        field = entry[0:3]  # All fields are three letters long
        fields.add(field)

    fields.discard("cid")  # We can ignore country of origin
    if fields == standard_set:
        total += 1

print(total)