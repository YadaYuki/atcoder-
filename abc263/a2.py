from collections import defaultdict
ABCDE = list(map(int,input().split()))

cards = defaultdict(int)

for c in ABCDE:
    cards[c] += 1

for k,v in cards.items():
    if not(v == 2 or v == 3):
        print("No")
        exit()
print("Yes")