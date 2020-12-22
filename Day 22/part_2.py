fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n\n")

from collections import deque

def deque_hash(deque1, deque2):
    copy1 = map(lambda x: str(x), list(deque1))
    copy2 = map(lambda x: str(x), list(deque2))
    return "P1: " + " ".join(copy1) + "P2: " + " ".join(copy2)


player1 = strs[0]
player2 = strs[1]
deck1 = [None] * 40
deck2 = [None] * 40
deck1[0] = deque()
deck2[0] = deque()
card1 = [0] * 40
card2 = [0] * 40
histories = [None] * 40
for card in player1.split('\n')[1:]:
    deck1[0].append(int(card))

for card in player2.split('\n')[1:]:
    deck2[0].append(int(card))

i = 0
histories[0] = []
while i >= 0:

    # check recursive victory
    if len(deck2[i]) == 0:
        i -= 1
        if i >= 0:
            deck1[i].append(card1[i])
            deck1[i].append(card2[i])
        continue
    elif len(deck1[i]) == 0:
        i -= 1
        if i >= 0:
            deck2[i].append(card2[i])
            deck2[i].append(card1[i])
        continue

    # check repeating previous configuration
    hash = deque_hash(deck1[i], deck2[i])
    if hash in histories[i]:
        i -= 1
        if i >= 0:
            deck1[i].append(card1[i])
            deck1[i].append(card2[i])
        continue
    histories[i].append(hash)


    # preserves card if recursing, overrides if not
    card1[i] = deck1[i].popleft()
    card2[i] = deck2[i].popleft()

    # do regular combat if uncopyable
    if len(deck1[i]) < card1[i] or len(deck2[i]) < card2[i]:
        if card1[i] > card2[i]:
            deck1[i].append(card1[i])
            deck1[i].append(card2[i])
        else:
            deck2[i].append(card2[i])
            deck2[i].append(card1[i])
    else:
        deck1[i+1] = deck1[i].copy()
        deck2[i+1] = deck2[i].copy()
        while len(deck1[i+1]) > card1[i]:
            deck1[i+1].pop()
        while len(deck2[i+1]) > card2[i]:
            deck2[i+1].pop()
        i += 1
        histories[i] = []  # start clean




winner_deck = deck1[0] + deck2[0]
deck_len = len(winner_deck)
total = 0
for i, card in enumerate(winner_deck):
    total += card * (deck_len - i)

print(total)