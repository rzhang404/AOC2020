fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n")

import re


nodes = set()
edges = set()
for rule in strs:
    outside, inside = rule.split(r"s contain")
    bags = set(re.split(r" [0-9] ", inside))
    bags.discard("")  # Discard empty string artifact from regex splitting
    bags.discard(" no other bags.")  # Discard a rule saying a bag contains no other bags

    outside = re.split(r" bags?", outside)[0]  # "[contains]... 1 bag" or "[contains]... 2 bags"
    nodes.add(outside)

    for bag in bags:
        ibag = bag[:-1]  # trim off , or .
        rebag = re.split(r" ba?g?s?", ibag)[0]
        nodes.add(rebag)
        edges.add((rebag, outside))

reachable = {"shiny gold"}
worklist = {"shiny gold"}

# curr_node = "shiny gold"
while len(worklist) > 0:
    curr_node = worklist.pop()
    for edge in edges:
        if edge[0] == curr_node and not reachable.__contains__(edge[1]):
            worklist.add(edge[1])
            reachable.add(edge[1])

reachable.discard("shiny gold")  # Cannot be the outermost
print(len(reachable))
print("hi")