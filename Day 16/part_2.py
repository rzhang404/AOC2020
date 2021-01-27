import collections

fo = open("input.txt", "r")
raw = fo.read()
sections = raw.split("\n\n")


# Note that all inputs are 1 - 999
possible_inputs = {*range(1000)}
criteria = sections[0].split("\n")
field_ranges = {}  # dict:  string -> []int
tickets = sections[2].split("\n")  # ignore our own
tickets = [x.split(",") for x in tickets[1:]]  # ignore "nearby tickets:"
unidentified_fields = set()
unidentified_indices = collections.deque(range(len(tickets[0])))  # set to length of one ticket

for criterion in criteria:
    field_name, rest = criterion.split(": ")
    range1, _or, range2 = rest.split(" ")
    lower, upper = range1.split("-")
    lower1i = int(lower)
    upper1i = int(upper)

    for i in range(lower1i, upper1i+1):
        possible_inputs.discard(i)

    lower, upper = range2.split("-")
    lower2i = int(lower)
    upper2i = int(upper)

    for i in range(lower2i, upper2i+1):
        possible_inputs.discard(i)

    field_ranges[field_name] = [lower1i, upper1i, lower2i, upper2i]
    unidentified_fields.add(field_name)

# prune out fully invalid tickets
valid_tickets = []
for ticket in tickets:
    for value in ticket:
        if int(value) in possible_inputs:  # misnomer: remaining things are not valid
            break
    else:  # if nothing calls for break
        valid_tickets.append(ticket)


# keep cycling through the field indices to find new fields to assign -- guaranteed to be doable, O(fn^2)
while len(unidentified_indices) > 0:
    candidate_index = unidentified_indices.popleft()
    possible_fields = unidentified_fields.copy()
    for ticket in valid_tickets:
        ticket_field_value = int(ticket[candidate_index])
        possible_fields_copy = possible_fields.copy()  # illegal to change size of set while iterating over it
        for field in possible_fields:
            lower1i, upper1i, lower2i, upper2i = field_ranges[field]
            # unwritten structure in input: all remaining values after discard are between highest upper1i
            # and lowest lower2i, so only the middle clause is actually relevant
            if ticket_field_value < lower1i or upper1i < ticket_field_value < lower2i or ticket_field_value > upper2i:
                possible_fields_copy.discard(field)

        possible_fields = possible_fields_copy  # possibly algorithmically costly, depending on memory writing cost

    if len(possible_fields) == 1:
        identified_field = possible_fields.pop()
        field_ranges[identified_field].append(candidate_index)
        unidentified_fields.discard(identified_field)
    else:
        unidentified_indices.append(candidate_index)

departure_fields = ["departure location", "departure station", "departure platform",
                    "departure track", "departure date", "departure time"]
our_ticket = sections[1].split("\n")[1].split(",")  # our ticket, as a list of fields
product = 1
for field in departure_fields:
    product *= int(our_ticket[field_ranges[field][4]])

print(product)
