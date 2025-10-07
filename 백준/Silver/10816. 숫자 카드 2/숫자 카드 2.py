n = int(input())
card_list = list(map(int, input().split()))

d = {}

for card in card_list:
    if card in d:
        d[card] = d[card] + 1
    else:
        d[card] = 1
        
m = int(input())

want_count = list(map(int, input().split()))

ans = [0 for _ in range(m)]

for idx, card in enumerate(want_count):
    if card in d:
        ans[idx] = d[card]

print(" ".join(map(str, ans)))
