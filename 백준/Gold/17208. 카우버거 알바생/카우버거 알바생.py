import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
datas = []
ans = 0

for i in range(n):
    x, y = map(int, input().split())
    if (x <= m and y <= k):
        datas.append((x, y))

n = len(datas)
dp = [[[0 for _ in range(n + 1)] for _ in range(k + 1)] for _ in range(m + 1)]

for z in range(1, n + 1):
    a, b = datas[z - 1]
    for x in range(0, m + 1):
        for y in range(0, k + 1):
            dp[x][y][z] = dp[x][y][z - 1]
            if (x - a >= 0 and y - b >= 0):
                dp[x][y][z] = max(dp[x][y][z], dp[x - a][y - b][z - 1] + 1)
            ans = max(ans, dp[x][y][z])

print(ans)
