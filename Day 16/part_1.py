fo = open("input.txt","r")
raw = fo.read()
sections = raw.split("\n\n")


# Note that all inputs are 1 - 999
possible_inputs = {*range(1000)}

criteria = sections[0].split("\n")
tickets = sections[2].split("\n")  # ignore our own
tickets = tickets[1:]  # ignore "nearby tickets:"

for criterion in criteria:
    field_name, rest = criterion.split(": ")
    range1, _or, range2 = rest.split(" ")
    lower, upper = range1.split("-")
    loweri = int(lower)
    upperi = int(upper)

    for i in range(loweri, upperi+1):
        possible_inputs.discard(i)

    lower, upper = range2.split("-")
    loweri = int(lower)
    upperi = int(upper)

    for i in range(loweri, upperi + 1):
        possible_inputs.discard(i)

scanning_error_rate = 0  # desired result
for ticket in tickets:
    for value in ticket.split(","):
        if int(value) in possible_inputs:
            scanning_error_rate += int(value)

print(scanning_error_rate)