n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

def comb(picked, idx, total):
    global ans
    if picked == 3:
        if total <= m:
            ans = max(ans, total)
        return
    for i in range(idx, n):
        comb(picked + 1, i + 1, total + arr[i])

comb(0, 0, 0)
print(ans)
