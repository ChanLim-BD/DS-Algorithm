N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

# print(cards)

sel = 0

for card in cards:
    if sel < min(card):
        sel = min(card)

print(sel)

####################

