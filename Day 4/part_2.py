fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n\n")

import re
total = 0
standard_set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",}
patterns = {
    "byr": "19[2-9][0-9]|200[0-2]",
    "iyr": "201[0-9]|2020",
    "eyr": "202[0-9]|2030",
    "hgt": "1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in",
    "hcl": "#([0-9]|[a-f]){6}",
    "ecl": "amb|blu|brn|gry|grn|hzl|oth",
    "pid": "[0-9]{9}",
    "cid": ".",
}
for passport in strs:
    entries = passport.split()
    fields = set()
    for entry in entries:
        field, value = entry.split(":")  # All fields are three letters long

        # If the field is invalid, break out immediately which will cause the valid fields test to field
        if not re.match(patterns[field], value):
            break

        fields.add(field)

    fields.discard("cid")  # We can ignore country of origin
    if fields == standard_set:
        total += 1

print(total)
