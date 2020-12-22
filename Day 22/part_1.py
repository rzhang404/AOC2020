fo = open("input.txt","r")
raw = fo.read()
strs = raw.split("\n\n")

from collections import deque


player1 = strs[0]
player2 = strs[1]
deck1 = deque()
deck2 = deque()
for card in player1.split('\n')[1:]:
    deck1.append(int(card))

for card in player2.split('\n')[1:]:
    deck2.append(int(card))

while len(deck1) > 0 and len(deck2) > 0:

    card1 = deck1.popleft()
    card2 = deck2.popleft()

    if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
    else:
        deck2.append(card2)
        deck2.append(card1)

winner_deck = deck1 + deck2
deck_len = len(winner_deck)
total = 0
for i, card in enumerate(winner_deck):
    total += card * (deck_len - i)

print(total)