fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n")

import re


nodes = {}
for rule in strs:
    outside, inside = rule.split(r"s contain")
    bags = set(re.split(r",|\.", inside))
    bags.discard("")  # Discard empty string artifact from regex splitting
    # bags.discard(" no other bags.")  # Discard a rule saying a bag contains no other bags

    outside = re.split(r" bags?", outside)[0]  # "[contains]... 1 bag" or "[contains]... 2 bags"
    nodes[outside] = []

    for bag in bags:
        bagnum = bag[1]
        ibag = bag[3:]  # trim off , or .
        rebag = re.split(r" bags?", ibag)[0]

        if bag != ' no other bags':
            nodes[outside].append((rebag, int(bagnum)))
        else:
            nodes[outside].append((rebag, -1))

total = 0
worklist = {"shiny gold": 1}

# curr_node = "shiny gold"
while len(worklist) > 0:
    curr_node = next(worklist.__iter__())
    curr_edges = nodes[curr_node]
    for edge in curr_edges:
        if edge[0] == " other":
            break
        worklist[edge[0]] = worklist.get(edge[0], 0) + worklist[curr_node] * edge[1]

    total += worklist[curr_node]
    del worklist[curr_node]

print(total)
print("hi")